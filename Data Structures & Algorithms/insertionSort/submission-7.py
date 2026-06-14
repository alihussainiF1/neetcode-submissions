# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []  # To store intermediate states

        for i in range(len(pairs)):
            j = i - 1
            current = pairs[i]
            
            # Move elements of pairs[0..i-1], that are greater than key, to one position ahead
            # of their current position
            while j >= 0 and current.key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1

            # Place the current element at its correct position
            pairs[j + 1] = current

            # Record the state after this insertion
            states.append(pairs[:])  # Use slicing to create a copy of the current state

        return states