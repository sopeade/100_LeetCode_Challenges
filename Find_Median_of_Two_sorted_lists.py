"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

# Basic Solution
# ----------------------------------------
# import numpy as np
# A = [1, 2, 4, 6, 7, 12, 15, 18, 20]
# B = [3, 4, 5, 9, 13, 15, 16, 17, 20, 21, 25, 28]
# C = A + B
# D = np.median(C)
# print(D)
# -----------------------------------------
#



# "Algorithmic Solution"
from collections import deque

A = deque([1, 2, 4, 6, 7, 12, 15, 18, 20])
B = deque([3, 4, 5, 9, 13, 15, 16, 17, 20, 21, 25, 28])
C = []

while B:
    if A:
        if B[0] < A[0]:
            C.append(B.popleft())
        elif B[0] == A[0]:
            C.append(B.popleft())
            C.append(A.popleft())
        else:
            C.append(A.popleft())
    else:
        C += B
        print("combined_string", C)
        break

if len(A) != 0:
    C += A
    print("combined_string", C)
if len(C) % 2 == 0:
    mid_length = int(len(C) / 2)
    median = (C[mid_length - 1] + C[mid_length]) / 2
else:
    mid_length = int(len(C) // 2)
    median = C[mid_length]

print(median)