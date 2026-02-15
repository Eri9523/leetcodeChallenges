""" 2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 """
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry: int = 0
        dummy: ListNode = ListNode(0)
        curr: ListNode = dummy
        while(l1 or l2 or carry):
            v1: int = l1.val if l1 else 0
            v2: int = l2.val if l2 else 0

            sum: int = v1 + v2 + carry

            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
    

    def array_to_listnode(self, arr: list):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


    def listnode_to_array(self, node: Optional[ListNode]) -> list:
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

mySolution = Solution()

l1_linked = mySolution.array_to_listnode(arr = [2,4,3])
l2_linked = mySolution.array_to_listnode(arr = [5,6,4])

mySolution.addTwoNumbers(l1 = l1_linked, l2 = l2_linked)

solutions = [
    {"l1": [2,4,3], "l2": [5,6,4], "expected": [7,0,8]},
    {"l1": [0], "l2": [0], "expected": [0]},
    {"l1": [9,9,9,9,9,9,9], "l2": [9,9,9,9], "expected": [8,9,9,9,0,0,0,1]},
]


for solution in solutions:
    l1_linked = mySolution.array_to_listnode(solution['l1'])
    l2_linked = mySolution.array_to_listnode(solution['l2'])
    
    result_node = mySolution.addTwoNumbers(l1_linked, l2_linked)
    
    result_arr = mySolution.listnode_to_array(result_node)
    
    assert result_arr == solution['expected'], (
        f"Error: {solution['l1']} + {solution['l2']} "
        f"expected {solution['expected']} but got {result_arr}"
    )

print("All tests passed")
