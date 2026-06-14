from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        pre_req_counter = [0]*numCourses

        for i in range(numCourses):
            adj[i]=[]

        for i in prerequisites: 
            x,y = i
            adj[y].append(x)
            pre_req_counter[x]+=1
        
        available = deque()
        order = [] 
        for i in range(len(pre_req_counter)):
            if pre_req_counter[i]==0:
                available.append(i)

        while available:
            og_course = available.popleft()
            order.append(og_course)
            print('t',og_course)
            if og_course in adj:
                og_list = adj[og_course]
                if og_list:
                    for x in og_list:
                        print(x)
                        pre_req_counter[x]-=1
                        if pre_req_counter[x]==0:
                            available.append(x)
                    print('ava',available)
            if len(order) == numCourses:
                return order
        return []