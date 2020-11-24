"""14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


output = ""
strs = ['flower', 'flow', 'flight']
for index in range(len(strs[0])):
    if len(set([i[index] for i in strs])) == 1:
        output += strs[0][index]
    else:
        print(output)
        break

"""
Note can also use 
for index in range(len(strs[0])):
    letter = strs[0][index]
    if all([i[index]=letter for i in strs]) == 1:
"""