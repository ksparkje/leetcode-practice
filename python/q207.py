# 207. Course Schedule
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have
# to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''walk through dfs
        '''
        so_far, req = [None] * numCourses, [[] for _ in range(numCourses)]
        # Initialize pre-requisites
        for to_take, prereq in prerequisites:
            req[to_take].append(prereq)

        def dfs(idx):
            '''
            While checking for a cycle,
                mark the current cycle as -1 in so_far
                if we run into -1, we return false
                elif 1, that means we have visited, so we can finish.
            After checking is done, mark this as 1, and return True
            '''
            cur_value = so_far[idx]
            if cur_value is not None:
                return cur_value == 1
            else: # We have not visited the current idx
                # Mark as currently visiting
                so_far[idx] = -1
                if req[idx].__len__() != 0:
                    no_cycle = all(dfs(to_visit) for to_visit in req[idx])
                    if not no_cycle: return False
                so_far[idx] = 1
                ret = [idx] + ret
                return True

        return all(dfs(idx) for idx in range(numCourses))


