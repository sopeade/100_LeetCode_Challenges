# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

highest_num = 0
a = "abdesbcdefart"
for index, letter_fl in enumerate(a):
    b = []
    for letter_sl in a[index:]:
        if letter_sl not in b:
            b.append(letter_sl)
            if len(b) > highest_num:
                # print("wow", len(b))
                highest_num = len(b)
                sub_string = b
        else:
            break
print(highest_num, sub_string)
