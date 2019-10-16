# A series of useful small functions

# Find two numbers in a list with the sum % val == 0
        d = collections.defaultdict(int)
        for i in nums:
            d[i % val] += 1
        
        ret = 0
        for k, v in d.items():
            if k == 0 or k == val // 2:
                ret += v*(v - 1) // 2
            elif (val - k) in d and val - k > k:
                ret += v * d[val - k]
        
        return ret
# Remove elements from set
set.discard(element)

# Combine two iterables using zip()
a = [1, 2, 3]
b = [4, 5, 6]
zip(a,b) # [(1,4), (2,5), (3,6)]

# find all factors of a given integer in order
def printDivisors(n):
    res = []
    list = []
    st = 2 if n % 2 == 0 else 3
    for i in range(st, int(math.sqrt(n) + 1), 2):   
        if (n % i == 0): 
            if (n / i != i):
                list.append(n//i)
            res.append(i)
    return res + list[::-1]
