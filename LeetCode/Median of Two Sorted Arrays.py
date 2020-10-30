'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

'''

# Solution

 def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # combine 2 arrays
        nums = nums1 + nums2
        #sort the array
        nums.sort()
        # call the length of the new array
        a = len(nums)
        # if the length is odd, we got the middle array by take out the int of half of the length
        if (a%2) != 0:
            b = int(a/2)
            return nums[b]
        # if the leng is even, we need to take two element and get avarage of them
        if a%2 ==0:
            b = int(a/2)
        return (nums[b] + nums[b-1])/2 
