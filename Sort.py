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
