# 947. Most Stones Removed with Same Row or Column
# Medium
#
# On a 2D plane, we place stones at some integer coordinate points.
# Each coordinate point may have at most one stone.
#
# Now, a move consists of removing a stone that shares a column
# or row with another stone on the grid.
#
# What is the largest possible number of moves we can make?

# Example 1:
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Example 2:
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Example 3:
#
# Input: stones = [[0,0]]
# Output: 0


'''
까다로운 문제...
'''


'''
This is from the Article
'''
class Solution:
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):  # for every stone
            for j in range(i):          # for stones below x
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:    # if in the same column or row
                    # Bi-directional edge
                    graph[i].append(j)              # stone_index == i: append index that corresponds
                    graph[j].append(i)              # stone_index == j:

        N = len(stones)
        ans = 0

        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not visited[nei]:
                            stack.append(nei)
                            visited[nei] = True
                ans -= 1
        return ans


'''
Another solution from the discussion
'''
class Solution:
    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)

        points, island, rows, cols = ({(i, j) for i, j in stones},
                                      0,
                                      collections.defaultdict(list),
                                      collections.defaultdict(list))
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island