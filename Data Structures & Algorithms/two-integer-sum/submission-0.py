class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive solution:
       for index, inum in enumerate(nums, start=0):
            for jndex, jnum in enumerate(nums, start=0):
                if index == jndex: continue
                elif inum + jnum == target: return [index, jndex]

