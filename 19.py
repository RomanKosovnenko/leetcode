# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        l_node = head
        r_node = head
        while r_node.next:
            if i > n:
                l_node = l_node.next
            i += 1
            r_node = r_node.next
        if l_node == head and i == n:
            return head.next
        else:
            l_node.next = l_node.next.next
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

def assetion(solution, listA, n, a):
    headA = generate_list(listA)
    answer = []
    sol = solution.removeNthFromEnd(headA, n)
    
    while sol:
        answer.append(sol.val)
        sol = sol.next
    assert answer == a

def test(solution, listA, n):
    answer = listA.copy()
    answer.pop(len(answer)-n)
    assetion(solution, listA, n, answer)

if __name__ == '__main__':
    solution = Solution()
    head = [1,2]
    n = 1
    test(solution, head, n)

    head = [1]
    n = 1
    test(solution, head, n)
    
    head = [1,2,3,4,5]
    n = 2
    test(solution, head, n)
    
    head = [1,2]
    n = 2
    test(solution, head, n)