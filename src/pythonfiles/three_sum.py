class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        CASE 1: 0 0 0
        CASE 2: -ve 0 +ve
        CASE 3: -VE -VE +VE
        CASE 4: +VE +VE -VE
        """
        output = []
        
        # CASE 5 (A+B)*-1 == C:
        if nums.count(0) >= 3:
            output.append([0,0,0])

        lst_set = set(nums)
        if nums.count(0) >= 1:
            for x in lst_set:
                if x*-1 in lst_set and x > 0:
                    if [-1*x,0,x] not in output:
                        output.append([-1*x,0,x])
        for x in nums:
            for y in nums:    
                if (y != 0 and x/y == -2 and nums.count(y) >= 2):
                    if [x,y,y] not in output:
                        output.append([x,y,y])
                for z in nums:
                    if (x+y+z) == 0 and abs(x) < abs(y) and abs(y) < abs(z) and abs(z) > abs(x):
                        if [x,y,z] not in output:
                            output.append([x,y,z])          
        return output