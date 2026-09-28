def make_api_request(endpoint, method, status_code, timeout, retries, headers):
    payload = {
        "endpoint": endpoint,
        "method": method,
        "expected_status": status_code,
        "timeout": timeout,
        "retries": retries,
        "headers": headers,
    }
    return payload


response = make_api_request(
    "/api/v1/auth/login",
    "POST",
    200,
    30.0,
    3,
    {"Content-Type": "application/json", "Authorization": "Bearer token_xyz"},
)
print(response)
