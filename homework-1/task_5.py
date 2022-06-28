import itertools as it
import math

def calculating_number(bases, values, limit):

  number = 1
  for base in range(len(bases)):
    number *= bases[base]**int(values[base])
  return number

def count_find_num(primesL, limit):


    base_dict = {}
    for base in primesL:
        base_dict[base] = math.floor(math.log(limit, base))

    string_dict = {}
    for i in base_dict.keys():
        string_dict[i] = [i for i in range(1, base_dict[i] + 1)]

    combinations = list(it.product(*string_dict.values()))

    spisok = []
    for i in combinations:
        num = calculating_number(primesL, i, limit)
        spisok.append(num)


    final_spisok = set([num for num in spisok if num <= limit])


    if len(final_spisok) != 0:
        return [len(final_spisok), max(final_spisok)]
    else:
        return []

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []