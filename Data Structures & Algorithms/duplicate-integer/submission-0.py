class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """ 
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
         
        """

        seen = []
        for i in nums:
            if i in seen:
                return True
            else:
                seen.append(i)
                continue
        return False
    
        