from redis_om import get_redis_connection, HashModel


redis_inv = get_redis_connection(
  host='redis-inventory-service',
  port=80
)
class Product(HashModel):
    name: str
    price: float
    quantity: int
    class Meta:
        database = redis_inv