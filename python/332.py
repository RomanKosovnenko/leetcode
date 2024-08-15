from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = {}
        n_flights = len(tickets)
        for dep, dest in sorted(tickets, reverse=True):
            if dep not in flights:
                flights[dep] = []
            flights[dep].append(dest)

        route = ["JFK"]
        itinerary = []

        while route:
            if route[-1] not in flights:
                itinerary.append(route.pop())
                continue
            if flights[route[-1]]:
                route.append(flights[route[-1]].pop())
                n_flights -= 1
            else:
                itinerary.append(route.pop())

        return itinerary[::-1]

s = Solution()
print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])) #["JFK","MUC","LHR","SFO","SJC"]
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])) #["JFK","ATL","JFK","SFO","ATL","SFO"]
print(s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])) #["JFK","NRT","JFK","KUL"]
