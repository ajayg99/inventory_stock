import redis
import time
from model import Order


redis_stream = redis.Redis(
  host='redis-stream-service',
  port=80,
  )

key = 'refund_order'
group = 'payment-group'


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
                order = Order.get(obj['pk'])
                order.status = 'refunded'
                order.save()

    except Exception as e:
        print(str(e))
    time.sleep(1)