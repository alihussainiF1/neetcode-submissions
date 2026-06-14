class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[] #pair of indices and the height value

        for i in range(len(heights)):
            start = i 
            while stack and stack[-1][1] > heights[i]:
                index,height_val = stack.pop()
                max_area = max(max_area,height_val*(i-index))
                start = index
            stack.append((start,heights[i]))
        for i in range(len(stack)):
            max_area=max(max_area,stack[i][1]*(len(heights)-stack[i][0]))
        return max_area
