# Subsets
'''
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

def subsets(nums):
    # output = [[]]
    # if len(nums) > 2:
    #     output.append(nums) 
        
    # for i in range(len(nums)):
    #     each = [nums[i]]
    #     output.append(list(each))
    #     each2 = [nums[i]]
    #     for j in range(i+1,len(nums)):
    #         each2.append(nums[j])
    #         output.append(list(each2))
    #         each2.pop()
    # return output
 
    output = [[]]
    for e in range(len(nums)):
        comp = nums[e:len(nums)]
        for i in range(len(comp),0,-1):
            each = []
            for j in range(0,i):
                each.append(comp[j])
            output.append(list(each))
    return output
    # 6 / 10 testcases passed

nums = [1,2,3]
print(subsets(nums))


'''''''''''''Check Test Cases'''''''''''''''
# Test Case 1
# input - [1,2,3]
# output - [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Test Case 2
# Input - [0]
# Output - [[],[0]]

# Test Case 3
# Input - [3,2,4,1]
# Output - [[],[3],[2],[2,3],[4],[3,4],[2,4],[2,3,4],[1],[1,3],[1,2],[1,2,3],[1,4],[1,3,4],[1,2,4],[1,2,3,4]]