import datetime
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple

#
# @dataclass
# class Movie:
#     title: str
#     dates: List[Tuple[datetime, datetime]]
#
#     def schedule(self) -> Generator[datetime, None, None]:
#         return []
#
#
# m = Movie('sw', [
#   (datetime(2020, 1, 1), datetime(2020, 1, 7)),
#   (datetime(2020, 1, 15), datetime(2020, 2, 7))
# ])
#
# for d in m.schedule():
#     print(d)

m = [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7)),
    (datetime(2020, 2, 15), datetime(2020, 2, 18))
 ]




for date in m:
    [print(date[0] + timedelta(i)) for i in range(((date[1] - date[0]).days)+ 1)]


