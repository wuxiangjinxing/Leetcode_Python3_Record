# Split an array into two subsets with equal sum

    def canPartition(self, nums: List[int]) -> bool:
        sum_val = sum(nums)
        if sum_val & 1 == 1:
            return False
        bits = 1
        for num in nums:
            #print(bin(bits), bin(bits << num), bin(bits | (bits << num)))
            #print((bits), (bits << num), (bits | (bits << num)))
            bits |= (bits << num)
            
        return bits >> (sum_val >> 1) & 1
