# Longest Substring Without Repeating Characters
''' Medium
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
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
""" Accepted 5.8M, Submissions 16.7M, Acceptance Rate 34.9% """

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempStr = ''
        check = set()
        pairs = []
        for i in s:
            if i not in check:
                check.add(i)
                tempStr += i
            else:
                pairs.append(tempStr)
                tempStr = pairs[-1].split(i)[-1] + i
        pairs.append(tempStr)
        return max(map(lambda x:len(x),pairs))

s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))