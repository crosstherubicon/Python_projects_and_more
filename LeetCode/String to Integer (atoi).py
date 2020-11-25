'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 or (len(s) > 0 and not (s[0] in ['+','-'] or s[0].isdigit())):
            return 0

        value = 0
        sign = -1 if s[0] == '-' else 1
        i = 1 if not s[0].isdigit() else 0

        while i < len(s) and s[i].isdigit():
            value = (value * 10) + (ord(s[i]) - ord('0'))
            i += 1
        value *= sign

        if value < -(2**31):
            return -(2**31)
        elif value > (2**31)-1:
            return (2**31)-1

        return value  
