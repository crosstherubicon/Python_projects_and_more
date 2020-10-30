'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 
 '''
# Solution

def threeSum(self, nums):
        occur = dict()
        Sout = set()
        
        for x in nums:
            if x in occur:
                occur[x] +=1
            else:
                occur[x] = 1
        
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                third = -nums[i]-nums[j]
                if  third in occur:
                    if nums[i] == 0 and nums[j] == 0 and occur[0] < 3: pass
                    elif nums[i] == nums[j] and occur[nums[i]] < 2: pass
                    elif nums[i] == third and occur[third] < 2: pass
                    elif nums[j] == third and occur[third] < 2: pass
                    else: Sout.add(tuple(sorted([nums[i],nums[j],third])))
                        
        return Sout
