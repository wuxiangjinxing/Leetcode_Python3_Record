# 354. Russian Doll Envelopes
# 952. Largest Component Size by Common Factor
# 684. Redundant Connection
# 685. Redundant Connection II

# Disjoint union set is a data structure that tracks a set of data partitioned in a number of non-overlapping subsets. 
# The data structure supports find (locate the subset for a given data) and union (combine two subsets) operations.
# Union-by-rank: 

class DSU:
    def __init__(self, nodes):
        self.par = list(range(nodes))
        self.rnk = [0] * nodes

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution:
    def yourfunction(self, data):
        dsu = DSU(len(data))
	
        
    
