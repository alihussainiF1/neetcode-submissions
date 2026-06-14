class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1] > heights[i]:
                index,height=stack.pop()
                max_area=max(max_area,height*(i-index))
                start = index

            stack.append((start,heights[i]))
        print(stack)
        for i in range(len(stack)):
            max_area=max(max_area,stack[i][1]*(len(heights)-stack[i][0]))
        return max_area
