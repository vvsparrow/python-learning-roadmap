import requests

url = "https://httpbin.org/get"
# headers = {"user-agent": "my-old-rusty-computer"}

r = requests.get(url)
print(r.text)
