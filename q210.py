# 210. Course Schedule II
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example 1
# Input: 2, [[1,0]]
# Output: [0,1]

# Example 2:
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

from collections import defaultdict


class SolutionMyLastAnswer:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:

        courses = [0 for _ in range(numCourses)]
        stack = []

        graph = defaultdict(list)
        for course, req in prerequisites:
            graph[req].append(course)

        def dfs(idx):
            if courses[idx] == -1:
                return False
            if courses[idx] == 1:
                return True
            courses[idx] = -1
            for next_course in graph[idx]:
                if not dfs(next_course):
                    return False
            stack.append(idx)
            courses[idx] = 1
            return True

        for idx in range(numCourses):
            if not dfs(idx):
                return []

        return stack[::-1]


class Solution:
    white, grey, black = range(3)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack_to_reverse = []
        nodes = {i: self.white for i in range(numCourses)}

        parent_to_child = defaultdict(list)
        for child, parent in prerequisites:
            parent_to_child[parent].add(child)

        def visit_node_return_true_if_cycle(node):
            nonlocal stack_to_reverse
            node_val = nodes[node]

            # Have not visited so visit them
            if node_val == self.white:
                nodes[node] = self.grey
                if any(visit_node_return_true_if_cycle(child)
                       for child in parent_to_child[node]):
                    return True
                stack_to_reverse += [node]
                nodes[node] = self.black

            elif node_val == self.grey:
                return True

        for node in nodes:
            if visit_node_return_true_if_cycle(node):
                return []
        return stack_to_reverse[::-1] if len(stack_to_reverse) == numCourses else []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        parent_counters = [0] * numCourses
        parent_to_children = [[] for _ in range(numCourses)]

        for child, parent in prerequisites:
            parent_counters[child] += 1
            parent_to_children[parent] += [child]

        # If parent_counter == 0, it's parent!
        toposort = [parent for parent in range(numCourses) if parent_counters[parent] == 0]

        node_idx = 0
        while node_idx < len(toposort):
            parent = toposort[node_idx]
            for child in parent_to_children[parent]:
                parent_counters[child] -= 1
                if parent_counters[child] == 0:
                    toposort += [child]
            node_idx += 1
        return toposort if len(toposort) == numCourses else []

