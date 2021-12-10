# Author: MOG 12/10/21

def three_letter_words(my_list):
    words = 0
    x = 0
    while x < len(my_list):
        if len(my_list[x]) == 3:
            words += 1
        x += 1
    return words



print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)