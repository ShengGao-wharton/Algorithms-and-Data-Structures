# You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
#
# You are also given a string s of length n, where s[i] is the character assigned to node i.
#
# Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.



class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        child = defaultdict(list)
        n = len(parent)

        for i in range(n):
            if parent[i] != -1:
                child[parent[i]].append(i)

        self.res = 1

        @lru_cache(None)
        def dfs(root, ch):
            if not child[root]:
                return 1
            first = 0
            second = 0
            for nei in child[root]:
                if s[nei] != ch:
                    path = dfs(nei, s[nei])

                    if path >= first:
                        first, second = path, first
                    elif path >= second:
                        first, second = first, path
            self.res = max(self.res, first + second + 1)
            return first + 1

        for i in range(n):
            dfs(i, s[i])

        return self.res

