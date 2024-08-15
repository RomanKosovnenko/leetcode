# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         hs = [0]*1001

#         for citation in citations:
#             for i in range(citation+1):
#                 hs[i] = hs[i] + 1
        
#         for i in range(1000, -1, -1):
#             if hs[i] >= i:
#                 return i

