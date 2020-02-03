def shift(lst, k):
    lst_copy = lst.copy()
    for ind in range(len(lst)):
        if ind + k < len(lst):
            lst[ind] = lst_copy[ind + k]
        else:
            lst[ind] = lst_copy[abs(len(lst) - (ind + k))]
    return lst


def directional_shift(lst, k, direction="left"):
    lst_copy = lst.copy()
    if direction == "right":
        k *= -1
    for ind in range(len(lst)):
        if ind + k < len(lst):
            lst[ind] = lst_copy[ind + k]
        else:
            lst[ind] = lst_copy[abs(len(lst) - (ind + k))]
    return lst
