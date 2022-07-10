def my_decorator(func):
    DICT = {}

    def wrapper(*args, **kwargs):
        key = int(*args)
        if key in DICT.keys():
            return DICT[key]
        result = func(*args, **kwargs)
        DICT[key] = result
        return result

    return wrapper


@my_decorator
def multiplier(number: int):
    return number * 2
"""
Надо написать декоратор для повторного выполнения декорируемой функции через некоторое время. Использует наивный 
экспоненциальный рост времени повтора (factor) до граничного времени ожидания (border_sleep_time).

В качестве параметров декоратор будет получать:

call_count - число, описывающее кол-во раз запуска функций;
start_sleep_time - начальное время повтора;
factor - во сколько раз нужно увеличить время ожидания;
border_sleep_time - граничное время ожидания.
Формула:

t = start_sleep_time * 2^(n) if t < border_sleep_time
t = border_sleep_time if t >= border_sleep_time

Кол-во запусков = call_count (допустим 3)
Начало работы
Запуск номер 1. Ожидание: t секунд. Результат декорируемой функций = func_result.
Запуск номер 2. Ожидание: t секунд. Результат декорируемой функций = func_result.
...
Конец работы"""

