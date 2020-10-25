# Add two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]


a = [1, 2, 3, 4, 5]
b = [2, 4, 5]
a.reverse()
b.reverse()
c = [str(value) for value in a]
d = [str(value) for value in b]
e = "".join(c)
f = "".join(d)
g= list(str(int(e) + int(f)))
print(a, b, g)

