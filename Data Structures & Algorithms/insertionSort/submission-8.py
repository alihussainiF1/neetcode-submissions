# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states= []

        for i in range(len(pairs)):
            j = i - 1 
            current = pairs[i]

            while j >= 0 and current.key < pairs[j].key:
                pairs[j+1]=pairs[j]
                j -= 1
            pairs[j+1] = current
            states.append(pairs[:])
        return states 