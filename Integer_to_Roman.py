"""12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.



Example 1:

Input: num = 3
Output: "III"

Example 2:

Input: num = 4
Output: "IV"

Example 3:

Input: num = 9
Output: "IX"

Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# Brute force solution. convert integers up to 3999
def convert(num):
    i = 0
    transform = ""
    while num:
        i += 1
        rem = num % 10
        if i == 1:
            if rem == 1:
                transform = 'I' + transform
            elif rem == 2:
                transform = 'II' + transform
            elif rem == 3:
                transform = 'III' + transform
            elif rem == 4:
                transform = 'IV' + transform
            elif rem == 5:
                transform = 'V' + transform
            elif rem == 6:
                transform = 'VI' + transform
            elif rem == 7:
                transform = 'VII' + transform
            elif rem == 8:
                transform = 'VIII' + transform
            elif rem == 9:
                transform = 'IX' + transform
        if i == 2:
            if rem == 1:
                transform = 'X' + transform
            elif rem == 2:
                transform = 'XX' + transform
            elif rem == 3:
                transform = 'XXX' + transform
            elif rem == 4:
                transform = 'XL' + transform
            elif rem == 5:
                transform = 'L' + transform
            elif rem == 6:
                transform = 'LI' + transform
            elif rem == 7:
                transform = 'LII' + transform
            elif rem == 8:
                transform = 'LIII' + transform
            elif rem == 9:
                transform = 'XC' + transform
        if i == 3:
            if rem == 1:
                transform = 'C' + transform
            elif rem == 2:
                transform = 'CC' + transform
            elif rem == 3:
                transform = 'CCC' + transform
            elif rem == 4:
                transform = 'CD' + transform
            elif rem == 5:
                transform = 'D' + transform
            elif rem == 6:
                transform = 'DI' + transform
            elif rem == 7:
                transform = 'DII' + transform
            elif rem == 8:
                transform = 'DIII' + transform
            elif rem == 9:
                transform = 'CM' + transform
        if i == 4:
            if rem == 1:
                transform = 'M' + transform
            elif rem == 2:
                transform = 'MM' + transform
            elif rem == 3:
                transform = 'MMM' + transform
        num = num // 10
    print(transform)