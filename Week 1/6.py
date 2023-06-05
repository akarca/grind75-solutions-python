"""
Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):




class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        return TreeNode(val=root.val, left=self.invertTree(root.right), right=self.invertTree(root.left))


def tree2list(root):
    if root.val:
        return []

    return [root.val] + tree2list(root.left) + tree2list(root.right)


def get_slice(level):
    if level == 0:
        return range(1)
    return range(pow(2, level) - 1, pow(2, level + 1) - 1)


def list2tree(l):
    """
    List to tree
    Level Order Binary Tree Traversal
    """
    i = 1
    tree_root = TreeNode(l[0])
    tree_elms = [tree_root]
    length = len(l)

    while True:
        index_slice = list(get_slice(i))
        root_slice = get_slice(i - 1)
        for root_index in root_slice:
            if root_index >= len(tree_elms):
                break

            root_elm = tree_elms[root_index]

            next_index = index_slice.pop(0)
            if next_index >= length:
                break

            left_node = TreeNode(l[next_index])
            if l[next_index]:
                root_elm.left = left_node
            tree_elms.append(left_node)

            next_index = index_slice.pop(0)
            if next_index >= length:
                break

            right_node = TreeNode(l[next_index])
            if l[next_index]:
                root_elm.right = right_node
            tree_elms.append(right_node)

        i += 1
        if i >= len(l):
            return tree_root


class TestCase(unittest.TestCase):
    def test_list2tree(self):
        tree_root = list2tree([4, 2, 7, 1, 3, 6, 9])


    def test_isPalindrome(self):
        sol = Solution()
        test_cases = [
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ]
        for case in test_cases:
            self.assertEqual(sol.isPalindrome(case[0]), case[1])


if __name__ == '__main__':
    unittest.main()
