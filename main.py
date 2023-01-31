

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
