def can_construct(word, letters):
    letters_list = list(letters)
    if len(word) > len(letters):
        return False
    try:
        for i in range(len(word)):
            if word[i] in letters_list:
                letters_list.remove(word[i])
    except ValueError:
        return False

    return True


print(can_construct("apples", "aples"))

print(can_construct("apples", "aplespl"))
