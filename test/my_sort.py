"""heap sort
   author: luochang212
   last update: 2020-06-20
"""

import random
import numbers


class SortTool():
    """sorting your list with 

    input: a list
    output: a sorted list

    usage: 
    st = SortTool()
    res = st.heap_sort(nums)
    """

    def heap_adjust(self, nums, s, t):
        """build heap"""
        rc = nums[s]
        i = s
        j = 2 * i
        while j <= t:
            if j < t and nums[j] < nums[j + 1]: 
                j += 1
            if rc > nums[j]:
                break
            nums[i] = nums[j]
            i = j
            j *= 2
        nums[i] = rc
        return nums

    def heap_sort(self, nums=None):
        """main"""
        if not nums:
            nums = [random.randint(0, 15) for _ in range(20)]
        if not all([isinstance(e, numbers.Number) for e in nums]):
            nums = [int(e) for e in nums]
        
        nums = [None]+nums
        n = len(nums) - 1
        for i in range(n // 2, 0, -1):
            nums = self.heap_adjust(nums, i, n)
        for i in range(n, 0, -1):
            nums[1], nums[i] = nums[i], nums[1]
            nums = self.heap_adjust(nums, 1, i - 1)
        
        return nums[1:]


def main():
    st = SortTool()
    res = st.heap_sort(["9", 3, 5, 1])
    print(res)


if __name__ == '__main__':
    main()
