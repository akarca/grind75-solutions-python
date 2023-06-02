"""
Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
"""
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> int:
        keys = {}
        for i in s:
            if not i in keys:
                keys[i] = 0

            keys[i] += 1

        length = 0
        odd_key = False
        for k in keys.keys():
            if keys[k] % 2 == 0:  # is even
                length += keys[k]
            else:
                if not odd_key:
                    length += 1
                    odd_key = True
                length += keys[k] - 1

        return length


class TestCase(unittest.TestCase):
    def test_longestPalindrome(self):
        sol = Solution()
        test_cases = [
            ("abccccdd", 7),
            ("a", 1),
            ("AABBaaa", 7),
            ("AaBbCcDd", 1),
            ("", 0),
        ]
        for case in test_cases:
            self.assertEqual(sol.longestPalindrome(case[0]), case[1])


if __name__ == '__main__':
    unittest.main()
