from redis_om import get_redis_connection, HashModel


redis_inv = get_redis_connection(
  host='redis-11804.c256.us-east-1-2.ec2.cloud.redislabs.com',
  port=11804,
  password="e58YcAo5M67OvWd7UZabr7o60XADlUBy"
)
class Product(HashModel):
    name: str
    price: float
    quantity: int
    class Meta:
        database = redis_inv