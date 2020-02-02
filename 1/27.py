lst = [1, 2, 3]
for elm in lst:
    elm = elm + 10

#wont work, not assigning to the items in the list

lst1 = [1, 2, 3]
lst2 = lst1
lst3 = [1, 2, 3]
lst1.append(4)
lst2.append(5)
lst3.append(6)
#lst1 = [1, 2, 3, 4, 5]
#lst2 = [1, 2, 3, 4, 5]
#lst3 = [1, 2, 3, 6]

s1 = 'abc'
s1.upper()

#s1 = 'abc' since s1.upper just creates a new string in the memory but s1 is not set to point to it


def main():
    lst = [1, 2, 3]
    s = 'abc'
    func(lst, s)
    print("main", lst, s)


def func(lst, s):
    lst.append(4)
    s = s.upper()
    print("func", lst, s)


main()

#prints func [1, 2, 3, 4] ABC then main [1, 2, 3, 4] abc since strings are immutable unlike lists, so the s in func ends up pointing to a different string in the memory
