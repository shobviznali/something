import math
import os

# 5


def sorting_lists(list1: list, list2: list):
    print(sorted(list1 + list2))
    print(sorted(list1 + list2, reverse=True))

# 7


def is_polindrom(str1: str) -> bool:
    reversed = str1[::-1]
    if str1 == reversed:
        return True
    return False


# 2


def is_date(days: int, month: int, year: int) -> bool:

    if month > 12 or days > 31:
        return False

    if month == 2 and is_year_leap(year) and days > 29:
        return False

    if month == 2 and not is_year_leap(year) and days > 28:
        return False

    list1 = [1, 3, 5, 7, 8, 10, 12]
    list2 = [2, 4, 6, 9, 11]
    set_months_with_31_days = set(list1)
    set_months_with_30_days = set(list2)

    if month in set_months_with_31_days and days > 31:
        return False

    if month in set_months_with_30_days and days > 30:
        return False

    return True


# 9


def is_year_leap(date: int) -> bool:
    if date % 4 == 0:
        return True
    return False


# 11


def square(side: float):


    per = 4 * side
    area = side * side
    diagonal = math.sqrt(side * side + side * side)

    my_tup = (per, area, diagonal)

    return my_tup

# 6


def is_prime(num: int):

    times = 1
    if num == 2:
        return True

    for i in range(1, int(num/2)):
        if num % i == 0:
            times += 1

    if times == 2:
        return True

    return False


# 12 если я правильно понял


turning_to_set = lambda list1 : set(list1)



# 1


def bank(money: float, years: int):

    for i in range(years):
        money = money + ((money * 10) / 100)
        years -= 1
        bank(money, years)

    return money

# 10


def common_elements(list1: list, list2: list) -> list:

    list1 = set(list1)
    list2 = set(list2)

    new_list = []
    for i in list1:
        if i in list2:
            new_list.append(i)

    return new_list



# 8


def razbienie(list1: list):

    first_list = []
    second_list = []
    third_list = []

    for i in range(0, int(len(list1) / 3)):
        first_list.append(list1[i])

    for i in range(int(len(list1) / 3), 2 * int(len(list1) / 3)):
        second_list.append(list1[i])

    for i in range(2 * int(len(list1) / 3), len(list1)):
        third_list.append(list1[i])

    first_list.reverse()
    second_list.reverse()
    third_list.reverse()

    list_of_lists = [first_list, second_list, third_list]

    return list_of_lists


# 3


def my_files(directory: str):


    if os.path.exists(directory):
        with os.scandir(directory) as files:
            for file in files:
                print(file.name)
    else:
        print('No such directory')


