from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


# 1-я Задача.
class CyclicIterator:
    def __init__(self, value_range):
        self.current = value_range[0] - 1
        self.value_range = value_range

        self.stop_value = value_range[-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        else:
            self.current = self.value_range[0] - 1
            self.current += 1
            return self.current


# 2-я Задача.
@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        # Создаются дни между двумя датами
        for date in self.dates:
            numdays = (date[1] - date[0]).days
            date_list = [date[0] + timedelta(days=x) for x in range(numdays + 1)]
            for day in date_list:
                yield day


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
