import time
from functools import wraps


def my_decorator(func):
    # Задача номер 1
    VALUES = {}

    def wrapper(*args, **kwargs):
        key = int(*args)
        if key in VALUES.keys():
            return VALUES[key]
        result = func(*args, **kwargs)
        VALUES[key] = result
        return result

    return wrapper


def repeater(call_count, start_sleep_time, factor, border_sleep_time):
    # Задача номер 2
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Начало работы')
            result = func(*args, **kwargs)
            t = start_sleep_time

            for n in range(1, call_count + 1):
                time.sleep(t)
                print(f'Запуск номер {n}. Ожидание: {t} секунд. Результат декорируемой функций = {result}.')

                t = t * 2 ** factor
                t = t if t < border_sleep_time else border_sleep_time

            return result

        return wrapper

    return decorator
