import requests

payload = {
    "name": "Vasya",
    "surname": "Pupkin",
}
try:
    r = requests.post(
        "https://httpbin.org/post",
    )
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"The request ended with an error: {err}")
