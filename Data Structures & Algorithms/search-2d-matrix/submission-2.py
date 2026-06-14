class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        row = None
        while top <=bottom :
            mid_row = (top+bottom)//2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else :
                print(matrix[mid_row])
                break 
        row = matrix[mid_row]

        if row is None:
            return False
        
        l,r = 0, len(row)-1
        while l<=r:
            mid = (l+r)//2
            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid -1 
            elif target == row[mid]:
                return True
        return False
