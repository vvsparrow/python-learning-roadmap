def log_success(test_name) -> None:
    test_name_upper = test_name.upper()
    print(f"*** [PASS] {test_name_upper} ***")


def log_failure(test_name) -> None:
    test_name_upper = test_name.upper()
    print(f"*** [FAIL] {test_name_upper} ***")


def format_log(status: str, test_name: str) -> str:
    test_name_upper = test_name.upper()
    return f"*** [{status}] {test_name_upper} ***"


def dry_log_success(test_name: str) -> None:
    print(format_log("PASS", test_name))


def dry_log_failure(test_name: str) -> None:
    print(format_log("FAIL", test_name))


if __name__ == "__main__":
    log_success("test_success")
    log_failure("test_failure")
    dry_log_success("dry_test_success")
    dry_log_failure("dry_test_failure")
