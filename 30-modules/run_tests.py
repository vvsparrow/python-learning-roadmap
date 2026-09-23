from api_helpers import format_auth_header

result = format_auth_header("qa-user-token")
assert result == {"Authorization": "Bearer qa-user-token"}

print("TEST PASSED: Header formatted correctly.")
