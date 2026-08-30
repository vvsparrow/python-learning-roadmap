import time


def retry(max_attempts, delay=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                result = func(*args, **kwargs)
                if result is not None:
                    return result
                attempts += 1
                time.sleep(delay)
            return None

        return wrapper

    return decorator


@retry(3, delay=2)
def some_function():
    return None


result = some_function()
print(result)
