class Solution:

    def searchInsert(self, nums, target):
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        if size == 0:
            return 0
        l = 0
        r = size
        # 搜索范围(l,r]

        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
        # return r也是正确的
