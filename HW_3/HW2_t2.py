from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Generator, List, Tuple


"""
Класс для парсинга сеансов фильма из List[Tuple[datetime, datetime]] 
и вывода всех дат, в которые фильм будет в кинотеатре, построчно.
"""
@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        # Функция пройдёт по всем датам и вернёт генератор, по которому в последствии пройдёмся для вывода дат.
        for i in range(len(self.dates)):

            start = self.dates[i][0]
            end = self.dates[i][1]
            while start <= end:
                yield start
                start += timedelta(days=1)


if __name__ == "__main__":
    m = Movie('sw', [
      (datetime(2020, 1, 1), datetime(2020, 1, 7)),
      (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    print(*m.schedule(), sep='\n')
