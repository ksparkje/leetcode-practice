# 341. Flatten Nested List Iterator

# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,4,6].


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class NestedIterator(object):
    def __init__(self, nestedList):
        self.nested = self.get_nested(nestedList)
        self.current_idx = 0

    def get_nested(self, nested_list):
        so_far = []
        for nl in nested_list:
            if nl.isInteger():
                so_far.append(nl.getInteger())
            else:
                so_far.extend(self.get_nested(nl.getList()))
        return so_far

    def next(self):
        next_item = self.nested[self.current_idx]
        self.current_idx += 1
        return next_item

    def hasNext(self):
        return self.current_idx < len(self.nested)


class NestedIterator(object):
    def __init__(self, nestedList):
        self.flat_list = self._flatten(nestedList)
        self.idx = -1

    def _flatten(self, l):
        so_far = []
        for elem in l:
            if elem.isInteger():
                so_far.append(elem.getInteger())
            else:
                so_far.extend(self._flatten(elem.getList()))
        return so_far

    def next(self):
        self.idx += 1
        return self.flat_list[self.idx]

    def hasNext(self):
        return self.idx < len(self.flat_list) - 1


def iterateNestedInteger(nested):
    if nested.isInteger():
        yield nested.getInteger()
    else:
        for child in nested.getList():
            yield from iterateNestedInteger(child)

def iterate(nestedList):
    for nested in nestedList:
        yield from iterateNestedInteger(nested)


class NestedIterator(object):
    def __init__(self, nestedList):
        self.gen = iterate(nestedList)
        self.value = None
        # Initialize your data structure here.

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.value

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        try:
            self.value = next(self.gen)
            return True
        except Exception as e:
            return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())















