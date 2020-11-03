import requests


def get_response_json():
    response = requests.get(
    "https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    return response.json()



for i in range(int(input("How many jokes?"))):
    print(get_response_json()["joke"], "\n")
