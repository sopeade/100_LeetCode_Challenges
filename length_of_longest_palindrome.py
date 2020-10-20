# Leetcode
# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
#
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.



word = "baabaab"
length_longestpalindrome = 0
longest_palindrome = ""
palindrome = []


for index, value in enumerate(word[:-1]):
    if word.count(value) > 1:
        box = []
        # box.append(value)
        palindrome_length = 0
        for other_index, other_value in enumerate(word[index:]):
            box.append(other_value)
            if value != other_value:
                pass
            else:
                if box[0:] == box[-1::-1]:
                    if len(box) > palindrome_length:
                        palindrome_length = len(box)
                        palindrome = "".join(box)

    if len(palindrome) > length_longestpalindrome:
        length_longestpalindrome = len(palindrome)
        longest_palindrome = palindrome
print(longest_palindrome, length_longestpalindrome)
