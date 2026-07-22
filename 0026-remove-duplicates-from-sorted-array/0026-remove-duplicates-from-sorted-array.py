class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the last placed unique element
        write_index = 0 
        
        # Scan through the array starting from the second element
        for read_index in range(1, len(nums)):
            # If a new unique element is found
            if nums[read_index] != nums[write_index]:
                write_index += 1
                nums[write_index] = nums[read_index]  # Modify in-place
                
        # Return the count of unique elements (index + 1)
        return write_index + 1