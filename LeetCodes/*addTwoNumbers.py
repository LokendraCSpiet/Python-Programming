# Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
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
'''
""" Accepted 4.6M, Submissions 10.7M, Acceptance Rate 43.0% """

from typing import Optional  # Need to import for local
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """ Method 1 : """
        # list1 = []
        # current_node = l1
        # while current_node is not None:
        #     list1.append(current_node.val)
        #     current_node = current_node.next

        # list2 = []
        # current_node2 = l2
        # while current_node2 is not None:
        #     list2.append(current_node2.val)
        #     current_node2 = current_node2.next

        # out = []
        # if len(list1) > len(list2):
        #     shortest = list2
        #     longest = list1
        # else:
        #     shortest = list1
        #     longest = list2

        # rem = 0
        # for i in range(len(shortest)):
        #     sum = shortest[i] + longest[i]
        #     if rem > 0:
        #         sum += rem
        #     rem = 0
        #     if sum > 9:
        #         sum -= 10
        #         rem = 1
        #     out.append(sum)

        # for j in range(len(shortest),len(longest)):
        #     sum = longest[j]
        #     if rem > 0:
        #         sum += rem
        #     rem = 0
        #     if sum > 9:
        #         sum -= 10
        #         rem = 1
        #     out.append(sum)

        # if rem > 0:
        #     out.append(rem)

        # head = ListNode(out[0])
        # tail = head
        # e=1
        # while e < len(out):
        #     tail.next = ListNode(out[e])
        #     tail = tail.next
        #     e+=1
        
        # return head
    
        """ Method 2 : """
        rem = 0
        node = ListNode()
        outNode = node
        while l1 is not None or l2 is not None or rem > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2
            if rem > 0:
               sum += rem
            rem = 0
            if sum > 9:
               sum -= 10
               rem = 1

            outNode.next = ListNode(sum)
            outNode = outNode.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return node.next
    
        """ ChatGPT's Code """
        # carry = 0
        # dummy_head = ListNode()
        # current = dummy_head
        
        # while l1 is not None or l2 is not None or carry != 0:
        #     val1 = l1.val if l1 else 0
        #     val2 = l2.val if l2 else 0
            
        #     total = val1 + val2 + carry
        #     carry = total // 10
        #     current.next = ListNode(total % 10)
        #     current = current.next

        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        
        # return dummy_head.next

def linked_list_to_list(head: ListNode) -> list:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Input -
# [2,4,3]
# [5,6,4]
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# Output - [7, 0, 8]

# Input -
# [2,4,9]
# [5,6,4,9]
l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
# Output - [7, 0, 4, 0, 1]

result = Solution().addTwoNumbers(l1, l2)
# print(result)

# For Local- 
print(linked_list_to_list(result))