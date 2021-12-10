# Author: MOG 12/10/21

def count_odds(my_list):
    odds = 0
    x = 0
    while x < len(my_list):
        if my_list[x] % 2 != 0:
            odds += 1
        x += 1
    return odds

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)