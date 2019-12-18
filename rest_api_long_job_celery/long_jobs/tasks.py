import random
from time import sleep

from celery import shared_task

DELAY_TIMES = [t for t in range(30, 60, 5)]


@shared_task()
def very_long_task():
    print('I am running')
    delay_in_seconds = random.choice(DELAY_TIMES)
    sleep(delay_in_seconds)
    return f'The job took {delay_in_seconds}'
