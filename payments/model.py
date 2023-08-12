from redis_om import get_redis_connection, HashModel


redis_payment = get_redis_connection(
  host='redis-payments-service',
  port=80
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