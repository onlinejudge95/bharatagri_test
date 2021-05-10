from functools import wraps
from random import uniform
from time import sleep


def exponential_backoff(retries=5, backoff=1):
    def decorated_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0

            while True:
                try:
                    result = func(*args, **kwargs)
                    return jsonify(result)
                except:
                    if count == retries:
                        raise RuntimeError("Reached maximum number of retries")

                    sleep_time = backoff * 2 ** count + uniform(0, 1)
                    print(f"Retrying in {sleep_time} s")
                    sleep(sleep_time)

                    count += 1

            return wrapper
        return decorated_function
    return exponential_backoff
