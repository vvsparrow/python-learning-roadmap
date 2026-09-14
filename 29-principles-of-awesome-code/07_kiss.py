def bad_has_failures(results: list[str]) -> bool:
    fail_count = 0
    for status in results:
        if status == "FAIL":
            fail_count += 1
    if fail_count > 0:
        return True
    else:
        return False


def kiss_has_failures(results: list[str]) -> bool:
    return "FAIL" in results


if __name__ == "__main__":
    print(bad_has_failures(["PASS", "PASS", "PASS", "FAIL", "PASS"]))
    print(kiss_has_failures(["PASS", "PASS", "PASS", "FAIL", "PASS"]))
