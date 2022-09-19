class Solution:
    # O(n log n) for sorting
    # O(1) for sorting in place
    # Total Time: 25 m - tried to come up with O(m+n) solution
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return