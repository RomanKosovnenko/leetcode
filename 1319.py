from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        array = list(range(n))
        ranks = [0]*n

        def find_parent(node):
            parent = array[node]
            return find_parent(parent) if node != parent else parent

        available_wires = 0
        def union(a, b):
            
            p_a = find_parent(a)
            p_b = find_parent(b)

            if p_a == p_b:
                return 1

            if ranks[p_a] >= ranks[p_b]:
                if ranks[p_a] == ranks[p_b]:
                    ranks[p_a] += 1
                array[p_b] = p_a
            else:
                array[p_a] = p_b
            return 0

        for connection in connections:
            available_wires += union(connection[0], connection[1])

        return available_wires if len(set(array)) <= available_wires+1 else -1
        
sol = Solution()
# print(sol.makeConnected(4, [[0,1],[0,2],[1,2]]))
# print(sol.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
# print(sol.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))
print(sol.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]))

