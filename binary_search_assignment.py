"""
    Question: You are given a list of numbers obtained by rotating a sorted list an unknown number
    of times. Write a function to determine the minimum number of times the original sorted list
    was rotated to obtain the given list. Your function should have the worst-case complexity of
    O(log N), where N is the length of the list. You can assume that all the numbers in the list
    are unique.

    Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list
    [0, 2, 3, 4, 5, 6, 9] 3 times.

    Solution:
    1. State the Problem: We need to find the number of times a given rotated sorted list was
       rotated.
    2. Come up with some example inputs and outputs. Try to cover all edge cases
        a. A list of size 10 rotated 3 times.
        b. A list that wasn't rotated at all.
        c. A list that was rotated just once.
        d. A list that was rotated `n-1` times, where n is the size of the list.
        e. A list that was rotated n times (do you get back the original list here?)
        f. An empty list.
        g. A list containing just one element.

"""

tests = [
    # A list of size 10 rotated 3 times.
    {
        'input': {
            'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
        },
        'output': 3
    },
    # A list that wasn't rotated at all.
    {
        'input': {
            'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
        },
        'output': 0
    },
    # A list that was rotated just once.
    {
        'input': {
            'nums': [10, 3, 5, 6]
        },
        'output': 1
    },
    # A list that was rotated `n-1` times
    {
        'input': {
            'nums': [5, 6, 7, 9, 11, 3]
        },
        'output': 5
    },
    # A list that was rotated n times
    {
        'input': {
            'nums': [3, 5, 6, 7, 9, 11]
        },
        'output': 0
    },
    # An empty list.
    {
        'input': {
            'nums': []
        },
        'output': 0
    },
    # A list containing just one element.
    {
        'input': {
            'nums': [4]
        },
        'output': 0
    },
]


def count_rotations(nums):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_num = nums[mid]
        if mid - 1 >= 0 and nums[mid - 1] > mid_num:
            return mid
        elif mid + 1 <= high and nums[mid + 1] > mid_num:
            high = mid - 1
        else:
            low = mid + 1
    return 0


if __name__ == '__main__':
    # for i, test in enumerate(tests):
    #     passed = count_rotations(**test['input']) == test['output']
    #     if passed:
    #         print(f"Test {i} Passed")
    #     else:
    #         print(f"Test {i} Failed")
    print(count_rotations(**tests[0]['input']))

