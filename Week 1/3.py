"""
Climbing Stairs
https://leetcode.com/problems/climbing-stairs

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return ListNode(val=list2.val, next=self.mergeTwoLists(list1, list2.next))

        if list2 is None:
            return ListNode(val=list1.val, next=self.mergeTwoLists(list1.next, list2))

        if list1.val <= list2.val:
            return ListNode(val=list1.val, next=self.mergeTwoLists(list1.next, list2))

        return ListNode(val=list2.val, next=self.mergeTwoLists(list1, list2.next))


def list2ln(l):
    if not l:
        return None

    if len(l) < 2:
        return ListNode(val=l[0], next=None)

    return ListNode(val=l[0], next=list2ln(l[1:]))


def ln2list(ln):
    if not ln:
        return []

    if not ln.next:
        return [ln.val]

    return [ln.val] + ln2list(ln.next)


def println(ln):
    if not ln:
        return None

    if not ln.next:
        return "%s" % ln.val

    return "%s, %s" % (ln.val, println(ln.next))


class TestCase(unittest.TestCase):
    def test_ln2list(self):
        root = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(val=3, next=ListNode(val=4)),
            ),
        )

        self.assertEqual(ln2list(root), [1, 2, 3, 4])

        root = ListNode(val=3, next=ListNode())

        self.assertEqual(ln2list(root), [3, 0])

        root = ListNode(val=1)

        self.assertEqual(ln2list(root), [1])

    def test_isValid(self):
        sol = Solution()
        test_cases = [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([1, 2, 4], [], [1, 2, 4]),
            ([], [0], [0]),
            ([], [], []),
        ]
        for case in test_cases:
            ln = sol.mergeTwoLists(list2ln(case[0]), list2ln(case[1]))
            self.assertEqual(ln2list(ln), case[2])


if __name__ == '__main__':
    unittest.main()
