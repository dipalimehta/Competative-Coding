# Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1
                        
                    
# Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j= len(nums)
        while i<j:
            if nums[i]==val:
                nums[i]=nums[j-1]
                nums[j-1]='_'
                j-=1
                i-=1
            i+=1
        return j
    
    