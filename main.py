

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


