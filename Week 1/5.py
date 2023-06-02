"""
Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]

        return s == s[::-1]


class TestCase(unittest.TestCase):
    def test_isPalindrome(self):
        sol = Solution()
        test_cases = [
            ("serdar", False),
            ("A man, a plan, a canal: Panama", True),
            ("serdar", False),
            (" ", True),
            (" he-l-:le-h", True),
            ("race a car", False),
            ("aATAa", True),
        ]
        for case in test_cases:
            self.assertEqual(sol.isPalindrome(case[0]), case[1])


if __name__ == '__main__':
    unittest.main()
