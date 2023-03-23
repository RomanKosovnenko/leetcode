# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        tmp = None
        while node and node.next:
            tmp = head if tmp else node
            head, node.next = node.next, node.next.next
            head.next= tmp
        return head

def generate_list(listA):
    headA = ListNode(0)
    c_A = headA
    iA = 0
    while iA < len(listA):
        c_A.next = ListNode(listA[iA])
        c_A = c_A.next
        iA += 1
    return headA.next

def assertion(solution, listA):
    headA = generate_list(listA)
    answer = []
    sol = solution.reverseList(headA)
    
    while sol:
        answer.append(sol.val)
        sol = sol.next
    assert answer == listA[::-1]

def test(solution, listA):
    assertion(solution, listA)

if __name__ == '__main__':
    solution = Solution()
    head = [1,2,3,4,5]
    test(solution, head)

    head = [1]
    test(solution, head)
    
    head = [1,2,3,4,5]
    test(solution, head)
    
    head = [1,2]
    test(solution, head)
    
    head = []
    test(solution, head)