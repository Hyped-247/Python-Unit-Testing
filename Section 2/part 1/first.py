"""
the avg function takes a list of numbers, and returns the their average.
@:return the average.
@:arg list of numbers.

Ex. print(avg(1, 2, 3, 43))
"""


def avg(*list_num):
    total = 0
    for num in list_num:
        total += num
    return total / len(list_num)
