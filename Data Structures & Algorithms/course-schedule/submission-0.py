class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={}
        for i in range(numCourses):
            preMap[i]=[]
        for item in prerequisites:
            print(item)
            course,pre_course=item
            preMap[course].append(pre_course)
        visitedSet=set()
        print(preMap)
        def dfs(course):
            if course in visitedSet:
                return False
            if preMap[course]==[]:
                print(course,'this')
                return True
            visitedSet.add(course) 
            for pre_req in preMap[course]:
                print(pre_req)
                if not dfs(pre_req):
                    return False
            visitedSet.remove(course)
            print(course)
            preMap[course]=[]
            return True

        
        for course in range(numCourses):
            print(course,'hihh')
            if not dfs(course):
                return False
        print(preMap)
        return True