#  Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast<len(nums):
            if nums[slow]!=nums[fast]:
                slow+=1
            nums[slow]=nums[fast]
            fast+=1
        return slow+1
    
    
# Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        count = 1

        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]:
                count += 1
            else:
                count = 1

            if count <= 2:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1