import datetime
import requests

now = datetime.datetime.now().timestamp()


def execution_time(func):
    def wrapper():
        start = datetime.datetime.now().timestamp()
        func()
        end = datetime.datetime.now().timestamp()
        print(f'Время выполнения: {end - start} секунд')
    return wrapper


@execution_time
def test_func():
    page = requests.get('https://google.com')
    print(page.status_code)


test_func()
