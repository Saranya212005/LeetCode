class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in nums:
            for j in str(i):
                l1.append(int(j))
        return l1
