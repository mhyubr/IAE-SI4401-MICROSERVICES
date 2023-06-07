from fastapi import FastAPI
from app.rajaongkir import get_shipping_cost, get_shipping_city

app = FastAPI()

@app.post("/shipping/cost")
def get_shipping(api_key: str, origin: str, destination: str, weight: int, courier: str):
    shipping_cost = get_shipping_cost(api_key, origin, destination, weight, courier)
    return {"shipping_cost": shipping_cost}

@app.get("/shipping/cities")
def get_shipping_cities(api_key: str, id: str, province: str):
    shipping_cities = get_shipping_city(api_key, id, province)
    return {"shipping_cities": shipping_cities}