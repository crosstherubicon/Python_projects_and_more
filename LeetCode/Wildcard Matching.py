'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
'''

#Solution 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        limitI = len(p) + 1
        limitJ = len(s) + 1
        dp = [[False for j in range(limitJ)] for i in range(limitI)]
        dp[0][0] = True
        
        for i in range(1, limitI):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
                
        for i in range(1, limitI):
            for j in range(1, limitJ):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                else: # isAlpha
                    if p[i - 1] == s[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[limitI - 1][limitJ - 1]
