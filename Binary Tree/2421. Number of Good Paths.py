class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        
        g = defaultdict(list)
        
        # start from node with minimum val
        for a, b in edges:
            heappush(g[a], (vals[b], b))
            heappush(g[b], (vals[a], a))

        
        loc = list(range(n))
        
        def find(x):
            if loc[x] != x:
                loc[x] = find(loc[x])
            return loc[x]
        
        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                loc[b] = a
        
        # node by val
        v = defaultdict(list)
        for i, val in enumerate(vals):
            v[val].append(i)
        
        ans = n
        
        
        for k in sorted(v):
            for node in v[k]:
                # build graph if neighboring node <= current node val
                while g[node] and g[node][0][0] <= k:
                    nei_v, nei = heappop(g[node])
                    union(node, nei)
            
            # Count unioned groups
            grp = Counter([find(x) for x in v[k]])
            
            # for each unioned group, select two nodes (order doesn't matter)
            ans += sum(math.comb(x, 2) for x in grp.values())            
        
        return ans