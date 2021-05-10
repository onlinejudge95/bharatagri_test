from random import uniform
from time import sleep

from src.app import create_celery


celery = create_celery()


def example_func(flag):
    if flag > 5:
        print("Call to the service succedded")
        return True
    raise ResourceWarning("Service is not responding")


@celery.task()
def simulated_task(flag, retries=5, backoff=1):
    count = 0
    while True:
        try:
            return example_func(flag)
        except ResourceWarning:
            if count == retries:
                raise RuntimeError("Reached maximum number of retries")

            sleep_time = backoff * 2 ** count + uniform(0, 1)
            print(f"Retrying in {sleep_time} s")
            sleep(sleep_time)

            count += 1
