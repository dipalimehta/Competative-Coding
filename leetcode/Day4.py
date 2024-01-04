# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0
        end = n-1
        middle = 0

        while middle<=end:
            if nums[middle] == 0:
                nums[start],nums[middle] = nums[middle],nums[start]
                start += 1
                middle += 1
            elif nums[middle] == 2:
                nums[end],nums[middle] = nums[middle],nums[end]
                end -= 1
            else:
                middle += 1
        return nums
    
    
    
    
# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        final_position = n-1

        for idx in range(n-2,-1,-1): #range(start,stop,step)--traverse backward
            if idx + nums[idx] >= final_position:
                final_position = idx

        if final_position==0:
            return True
        else:
            return False