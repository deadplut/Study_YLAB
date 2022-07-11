from hw_2 import *
from hw_3 import *

cyclic_iterator = CyclicIterator(range(3))

m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])


@my_decorator
def multiplier_1(number: int):
    return number * 2


@repeater(10, 2, 3, 25)
def multiplier_2(number: int):
    return number * 2


if __name__ == '__main__':

    # 2.1
    for i in cyclic_iterator:
        print(i)

    # 2.2
    for d in m.schedule():
        print(d)


    # 3.1
    multiplier_1(7)
    multiplier_1(7)
    multiplier_1(1)

    # 3.2

    multiplier_2(5)


