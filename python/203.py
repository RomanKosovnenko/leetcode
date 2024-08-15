# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode], val) -> Optional[ListNode]:
        node = ListNode(None)
        node.next = head
        tmp = node
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return tmp.next

def generate_list(listA):
    headA = ListNode(0)
    c_A = headA
    iA = 0
    while iA < len(listA):
        c_A.next = ListNode(listA[iA])
        c_A = c_A.next
        iA += 1
    return headA.next

def assertion(solution, listA, val):
    headA = generate_list(listA)
    answer = []
    sol = solution.reverseList(headA, val)
    listA = [i for i in listA if i != val]
    while sol:
        answer.append(sol.val)
        sol = sol.next
    assert answer == listA

def test(solution, listA, val):
    assertion(solution, listA, val)

if __name__ == '__main__':
    solution = Solution()
    head = [1,2,3,4,5,6]
    test(solution, head, 6)

    head = [7,7,7,7]
    test(solution, head, 7)
    
    head = [1,2,3,4,5]
    test(solution, head, 2)
    
    head = [1,2]
    test(solution, head, 1)
    
    head = []
    test(solution, head, 1)