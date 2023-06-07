import requests

def get_shipping_cost(api_key: str, origin: str, destination: str, weight: int, courier: str):
    url = "https://api.rajaongkir.com/starter/cost"
    payload = {
        "origin": origin,
        "destination": destination,
        "weight": weight,
        "courier": courier
    }
    headers = {
        "content-type": "application/json",
        "key": api_key,
    }
    response = requests.post(url, data=payload, headers=headers)
    print(response)
    response_data = response.json()
    # shipping_cost = None
    # if response_data["rajaongkir"]["status"]["code"] == 200:
    #     results = response_data["rajaongkir"]["results"]
    #     if len(results) > 0:
    #         shipping_cost = results[0]["costs"][0]["cost"][0]["value"]
    # return shipping_cost
    return response_data