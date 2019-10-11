# A series of useful small functions

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
