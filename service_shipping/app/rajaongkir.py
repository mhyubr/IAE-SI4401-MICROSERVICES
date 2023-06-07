import requests

def get_shipping_cost(api_key: str, origin: str, destination: str, weight: int, courier: str):
    url = "https://api.rajaongkir.com/starter/cost"
    # payload = {
    #     "Origin": origin,
    #     "Destination": destination,
    #     "Weight": weight,
    #     "Courier": courier
    # }
    payload = f"origin={origin}&destination={destination}&weight={weight}&courier={courier}"
    headers = {
        "content-type": "application/x-www-form-urlencoded ",
        "key": api_key,
    }
    response = requests.post(url, data=payload, headers=headers)
    response_data = response.json()
    shipping_cost = None
    if response_data["rajaongkir"]["status"]["code"] == 200:
        results = response_data["rajaongkir"]["results"]
        if len(results) > 0:
            shipping_cost = results[0]["costs"][0]["cost"][0]["value"]
    elif response_data["rajaongkir"]["status"]["code"] == 400:
        return response_data["rajaongkir"]["status"]["description"]
    return shipping_cost
    # return {"Origin": origin, "Destination": destination, "Weight": weight, "Courier": courier}

def get_shipping_city(api_key: str, id: str, province: str):
    url = "	https://api.rajaongkir.com/starter/city"

    payload = f"id={id}&province={province}"
    headers = {
        "content-type": "application/x-www-form-urlencoded ",
        "key": api_key,
    }

    response = requests.get(url, params=payload, headers=headers)
    response_data = response.json()
    shipping_city = None

    if response_data["rajaongkir"]["status"]["code"] == 200:
        results = response_data["rajaongkir"]["results"]
        if len(results) > 0:
            shipping_city = [city["city_name"] for city in results]
    elif response_data["rajaongkir"]["status"]["code"] == 400:
        return response_data["rajaongkir"]["status"]["description"]

    return shipping_city

    # return response_data["rajaongkir"]["results"]