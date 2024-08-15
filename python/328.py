# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even

        while odd.next is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
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

def get_answer(sol):
    odd = []
    even = []
    i = 1
    while sol:
        if i % 2 == 1:
            odd.append(sol.val)
        else:
            even.append(sol.val)
        sol = sol.next
        i += 1

    return odd+even

def get_list(sol):
    answer = []
    while sol:
        answer.append(sol.val)
        sol = sol.next
    return answer

def assertion(solution, listA):
    headA = generate_list(listA)

    answer = get_answer(headA)
    sol = solution.oddEvenList(headA)
    sol = get_list(sol)
    

    assert answer == sol

def test(solution, listA):
    assertion(solution, listA)

if __name__ == '__main__':
    solution = Solution()
    head = [1,2,3,4,5]
    test(solution, head)

    head = [1]
    test(solution, head)

    head = []
    test(solution, head)

    head = [2,1,3,5,6,4,7]
    test(solution, head)