class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique = list(set(nums))
        unique.sort(reverse = True)
        if len(unique)>= 3:
            return unique[2]
        else:
            return unique[0]
            
        
        
        