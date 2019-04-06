# https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6


def monotonic_increasing(given_array):
    # stack with (index, item)
    increasing = []

    length = len(given_array)
    first_smaller_on_left = [-1] * length
    first_smaller_on_right = [-1] * length

    for idx, item in enumerate(given_array):
        while increasing and increasing[-1][1] >= item:
            # Queue with (index, item)
            first_smaller_on_right[increasing.pop()[0]] = item

        if increasing:
            # current item is not in the queue yet
            first_smaller_on_left[idx] = increasing[-1][1]

        increasing.append([idx, item])

    return first_smaller_on_left, first_smaller_on_right


def monotonic_decreasing(given_array):
    decreasing = []

    length = len(given_array)
    first_elem_larger_on_left = [-1] * length
    first_elem_larger_on_right = [-1] * length

    for idx, item in enumerate(given_array):
        while decreasing and decreasing[-1][1] <= item:
            first_elem_larger_on_right[decreasing.pop()[0]] = item

        if decreasing:
            first_elem_larger_on_left[idx] = decreasing[-1][1]

        decreasing.append([idx, item])

    return first_elem_larger_on_left, first_elem_larger_on_right


if __name__ == '__main__':
    A = [5, 3, 1, 2, 4]
    print(monotonic_increasing(A))
    print(monotonic_decreasing(A))
