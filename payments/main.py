from fastapi import FastAPI
from model import Order
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from starlette.requests import Request
import requests, time, redis

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #allow frontend to request the API 
    allow_methods=['*'],
    allow_headers=['*']
)


redis_stream = redis.Redis(
  host='redis-stream-service',
  port=80,
  )


@app.get('/orders/{pk}')
def get(pk: str):
    order = Order.get(pk)
    return order


@app.post('/orders')
async def create(request: Request, background_task: BackgroundTasks):
    body = await request.json()
    product_url = 'http://inv-app-service/products/%s' % body['id']
    req = requests.get(product_url)
    product = req.json()
    order = Order(
        product_id = body['id'],
        price = product['price'],
        fee = 0.1*product['price'],
        total = 1.2*product['price'],
        quantity=body['quantity'],
        status='pending'
    )
    order.save()

    background_task.add_task(order_complete, order)   #runs in the background

    return order


def order_complete(order: Order):
    time.sleep(5)  # to add real time delay
    order.status = 'completed'
    order.save()
    redis_stream.xadd('order_completed', order.dict(),'*')  #msg, order, id(* - authogenerated) #this is a event and conusmer is on inventory/conusmer.py