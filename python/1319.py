from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n-1 > len(connections):
            return -1
        array = list(range(n))

        def find_parent(node):
            parent = array[node]
            if node != parent:
                parent = find_parent(parent)
                array[node] = parent
            return parent

        available_wires = 0
        def union(a, b):
            
            p_a = find_parent(a)
            p_b = find_parent(b)

            if p_a == p_b:
                return 1

            array[p_b] = p_a
            return 0

        for connection in connections:
            available_wires += union(connection[0], connection[1])
        
        networks = set()
        
        for node in array:
            networks.add(find_parent(node))

        return len(networks)-1
        
sol = Solution()
print(sol.makeConnected(4, [[0,1],[0,2],[1,2]]))
print(sol.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(sol.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))
print(sol.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]))
print(sol.makeConnected(12, [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))

