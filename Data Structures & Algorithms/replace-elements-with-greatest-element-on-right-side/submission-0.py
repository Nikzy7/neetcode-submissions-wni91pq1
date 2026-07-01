class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        toRet = []

        for x in range(len(arr)):
            currMax = -1
            for y in range(x+1,len(arr)):
                currMax = max(currMax,arr[y])
            toRet.append(currMax)

        return toRet