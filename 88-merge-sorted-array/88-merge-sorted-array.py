class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Total Time: 12 m
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        left, right, end = m - 1, n - 1, len(nums1) - 1
        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[end] = nums1[left]
                left -= 1
            else:
                nums1[end] = nums2[right]
                right -= 1
            end -= 1
                
        