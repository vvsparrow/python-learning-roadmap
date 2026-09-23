def format_auth_header(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


if __name__ == "__main__":
    print(format_auth_header("test-secret-123"))
