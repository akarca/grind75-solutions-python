"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {"{": "}", "}": "{", "[": "]", "]": "[", "(": ")", ")": "("}
        lchars = {"{": True, "[": True, "(": True, "}": False, "]": False, ")": False}

        for c in s:
            if lchars[c]:
                stack.append(c)
            elif not stack or stack.pop() != chars[c]:
                return False

        return not stack


class TestCase(unittest.TestCase):
    def test_isValid(self):
        sol = Solution()
        self.assertEqual(sol.isValid(""), True)
        self.assertEqual(sol.isValid("()"), True)
        self.assertEqual(sol.isValid("()[]{}"), True)
        self.assertEqual(sol.isValid("[([{}])[]][{}][]"), True)
        self.assertEqual(sol.isValid("([{}])({{{}}})[[[]]]"), True)
        self.assertEqual(sol.isValid("(([]){}"), False)
        self.assertEqual(sol.isValid("[["), False)
        self.assertEqual(sol.isValid("{]}"), False)
        self.assertEqual(sol.isValid(")"), False)
        self.assertEqual(sol.isValid("{{}}}"), False)
        self.assertEqual(sol.isValid("[][(]"), False)
        self.assertEqual(sol.isValid("{}}}}"), False)
        self.assertEqual(sol.isValid("}}}"), False)
        self.assertEqual(sol.isValid(")()"), False)
        self.assertEqual(sol.isValid("[[()]]{"), False)
        self.assertEqual(sol.isValid("[]{}[[]"), False)


if __name__ == '__main__':
    unittest.main()
