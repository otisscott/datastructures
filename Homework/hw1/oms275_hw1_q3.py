def sum_of_squares(n):
    total = 0
    for itr in range(n):
        total += itr**2
    return total


def sum_of_squares_list_comp(n):
    return [itr**2 for itr in range(n)]


def sum_of_odd_squares(n):
    total = 0
    for itr in range(1, n, 2):
        total += itr**2
    return total


def sum_of_odd_squares_list_comp(n):
    return [itr**2 for itr in range(1, n, 2)]
