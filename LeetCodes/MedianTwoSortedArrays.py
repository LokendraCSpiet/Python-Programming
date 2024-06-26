# Find Median Sorted Arrays
''' Hard
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

""" Accepted 2.6M, Submissions 6.5M, Acceptance Rate 40.2% """




class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2 == 0:
            return (nums1[len(nums1)//2] + nums1[(len(nums1)//2) - 1]) / 2
        else:
            return nums1[len(nums1)//2]


nums1 = [3]
nums2 = [2,7]

# nums1 = [3]
# nums2 = [-2,-1]
# # output = -1
print(Solution().findMedianSortedArrays(nums1,nums2))
