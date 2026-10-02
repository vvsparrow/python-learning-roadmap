import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

try:
    r = requests.get(url, params=params, timeout=5)
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Request failed: {err}")
else:
    print(f"Success! Status code: {r.status_code}")
    posts = r.json()
    print(f"Total posts received: {len(posts)}")
    print(f"First post title: {posts[0]['title']}")
    for post in posts:
        assert post["userId"] == 1
    print("Verification passed: all posts belong to userId 1.")
