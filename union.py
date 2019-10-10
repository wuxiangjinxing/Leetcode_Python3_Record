# 354. Russian Doll Envelopes
# 952. Largest Component Size by Common Factor
# 684. Redundant Connection
# 685. Redundant Connection II

# Disjoint union set is a data structure that tracks a set of data partitioned in a number of non-overlapping subsets. The data structure supports find (locate the subset for a given data) and union (combine two subsets) operations.

class DSU:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = collections.defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
	
    def find(self, subsets, i):
        if subsets[i] == -1:
            return i
        else:
            return self.find(subsets, subsets[i])
        
    def union(self, subsets, x, y):
        x_set = self.find(subsets,x)
        y_set = self.find(subsets,y)
        subsets[x_set] = y_set
	
	
        
    
