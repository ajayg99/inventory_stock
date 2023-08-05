from fastapi import FastAPI
from model import Product
import redis_om
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend-inv-service.invstockprod.svc.cluster.local", "http://frontend-ord-service.invstockprod.svc.cluster.local"],  #allow frontend to request the API
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/products/{pk}')
def get_product(pk: str):
    try:
        return Product.get(pk)
    except redis_om.model.model.NotFoundError:
            return {"error": "Product not found"}

@app.get('/products')
def all():
    return [format(pk) for pk in Product.all_pks()]

def format(pk: str):
     product = Product.get(pk)
     return {
          'id': product.pk,
          'name': product.name,
          'price': product.price,
          'quantity': product.quantity
     }

@app.post('/products')
def create(product: Product):
    return product.save()

@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)