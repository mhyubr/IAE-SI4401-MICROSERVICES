from fastapi import FastAPI
from app.rajaongkir import get_shipping_cost

app = FastAPI()

@app.post("/shipping")
def get_shipping(api_key: str, origin: str, destination: str, weight: int, courier: str):
    shipping_cost = get_shipping_cost(api_key, origin, destination, weight, courier)
    return {"shipping_cost": shipping_cost}