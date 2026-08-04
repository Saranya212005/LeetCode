class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # max_avg=float('-inf')
        # for i in range(len(nums)):
        #     curr_avg=0
        #     if (i+k)<=len(nums):
        #         for j in range(i,i+k):
        #             curr_avg+=nums[j]
        #         curr_avg=curr_avg/k
        #         if curr_avg>max_avg:
        #             max_avg=(curr_avg)
        #     i+=1
        # return max_avg


        # max1=0
        # n=len(nums)-k+1
        # for i in range(n):
        #     sum1=sum(nums[i:k+i])
        #     avg=sum1/k
        #     max1=max(max1,avg)

        # return max1


        w=0
        max1=0
        for i in range(k):
            w+=nums[i]
        sm=w
        for i in range(k,len(nums)):
            w=w-nums[i-k]+nums[i]
            sm=max(w,sm)
        return sm/k