
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]


    def schedule(self) -> List[List[datetime]]:  #Generator[datetime, None, None]:
        dates: List[Tuple[datetime, datetime]] = self.dates

        return [[date1 + timedelta(i) for i in range((date2 - date1).days + 1)] for date1, date2 in dates]




m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for date in m.schedule():
    print(*date, sep='\n')


# m = [
#     (datetime(2020, 1, 1), datetime(2020, 1, 7)),
#     (datetime(2020, 1, 15), datetime(2020, 2, 7)),
#  ]
#

# for date in m:
#     [print(date[0] + timedelta(i)) for i in range(((date[1] - date[0]).days)+ 1)]


