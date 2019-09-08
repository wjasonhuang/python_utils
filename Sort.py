'----------sort with lambda and cmp----------'
nums = [(8, 9), (4, 13), (4, 15), (8, 2), (13, 4), (1, 17), (18, 18), (4, 12)]
print(sorted(nums, key=lambda item: item[1]-item[0]))

from functools import cmp_to_key
def sort_by_diff(nums):
    def cmp(a, b): return (a[1]-a[0]) - (b[1]-b[0])
    return sorted(nums, key=cmp_to_key(cmp))
print(sort_by_diff(nums))

'----------quick sort----------'
import random
def quick_sort(nums):
    def sort(l, r):
        if l < r:
            p = random.randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            k, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[k] = nums[k], nums[i]
                    k += 1
            nums[k], nums[r] = nums[r], nums[k]
            sort(l, k-1)
            sort(k+1, r)
    sort(0, len(nums)-1)

'----------merge sort----------'
def merge_sort(nums):
    ret = [0] * len(nums)
    def sort(l, r):
        if l < r:
            m = (l + r) // 2
            sort(l, m)
            sort(m+1, r)
            p, p1, p2 = l, l, m+1
            while p1 <= m and p2 <= r:
                if nums[p1] < nums[p2]:
                    ret[p] = nums[p1]
                    p1 += 1
                else:
                    ret[p] = nums[p2]
                    p2 += 1
                p += 1
            while p1 <= m:
                ret[p] = nums[p1]
                p1 += 1
                p += 1
            while p2 <= r:
                ret[p] = nums[p2]
                p2 += 1
                p += 1
            nums[l:r+1] = ret[l:r+1]
    sort(0, len(nums)-1)
