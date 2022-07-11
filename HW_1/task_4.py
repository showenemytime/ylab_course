from itertools import combinations


def bananas(s) -> set:
    result = set()
    for i in combinations(range(0, len(s)), len(s) - 6):  # задаю диапозон
        m = list(s)
        for j in i: m[j] = '-'  # перебераю
        if [k for k in m if k != '-'] == list('banana'): result.add(''.join(m))  # если == банана, добавляю в сет
    return result
# print(*bananas(input()), sep='\n')


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
