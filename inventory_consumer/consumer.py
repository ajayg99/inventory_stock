import redis
from model import Product
import time


redis_stream = redis.Redis(
  host='redis-stream-service',
  port=80,
  )

key = 'order_completed'
group = 'inventory-group'

try:
    redis_stream.xgroup_create(key,group,'$',mkstream=True)
except:
    print('group already exist')

while True:
    try:
        results = redis_stream.xreadgroup(group, key, {key: '>'},None)
        if results!=[]:
            for items in results:
                obj = items[1][0][1]
                obj = {k.decode('utf-8'): v.decode('utf-8') for k, v in items[1][0][1].items()}
                try:
                    product = Product.get(obj['product_id'])
                    product.quantity = product.quantity - int(obj['quantity'])
                    product.save()
                except:
                    redis_stream.xadd('refund_order',obj,'*')
    except Exception as e:
        print(str(e))
    time.sleep(1)