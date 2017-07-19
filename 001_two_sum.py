class Solution:
    class Item:
        def __init__(self, value, index):
            self.value = value
            self.index = index
            
    def twoSum(self, nums, target):
        len_num = len(nums)
        if len_num == 0 or len_num == 1:
            return [-1, -1]
        
        items = [Solution.Item(value, 0) for value in nums]
        for i in range(0, len_num):
            items[i].index = i
        items.sort(lambda x, y: cmp(x.value, y.value))
        index1 = 0
        index2 = len_num - 1
        is_find = False
        while index1 < index2:
            total = items[index1].value + items[index2].value
            if total < target:
                index1 += 1
            elif total > target:
                index2 -= 1
            else:
                is_find = True
                break
        if is_find == True:
            return [items[index1].index, items[index2].index]
        else:
            return [-1, -1]
            
