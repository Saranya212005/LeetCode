class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left():
            low=0
            high=len(nums)-1
            val1=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    val1=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return val1
        def right():
            low=0
            high=len(nums)-1
            val=-1           
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    val=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return val
        l1=left()
        l2=right()
        
        return l1,l2