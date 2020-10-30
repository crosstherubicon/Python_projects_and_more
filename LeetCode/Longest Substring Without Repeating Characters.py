# Longest Substring Without Repeating Characters
'''

Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

## Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        maxi = 0
        start = 0
        for i, char in enumerate(s):
            if char not in s[start:i]: counter += 1
            else:
                maxi = max(maxi, counter)
                start = s.find(char, start) + 1
                counter = len(s[start: i + 1])
        return max(maxi, counter)
