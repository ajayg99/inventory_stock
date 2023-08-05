from redis_om import get_redis_connection, HashModel


redis_payment = get_redis_connection(
  host='redis-11804.c256.us-east-1-2.ec2.cloud.redislabs.com',
  port=11804,
  password="e58YcAo5M67OvWd7UZabr7o60XADlUBy"
)
class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str #pending, completed, refunded

    class Meta:
        database = redis_payment