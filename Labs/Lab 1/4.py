import random


def create_permutation(n):
    lst = [random.randint(0, i) for i in range(n)]
    return lst


print(create_permutation(6))
