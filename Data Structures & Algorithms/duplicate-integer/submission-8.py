class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list= []
        for i in nums:
            if i not in my_list:
                my_list.append(i)
            else:
                return True
        return False
