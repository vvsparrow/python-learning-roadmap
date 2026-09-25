import requests

response = requests.get("https://sparrowlab.dev")
assert response.status_code == 200

print("SMOKE TEST PASSED: sparrowlab.dev is alive!")
