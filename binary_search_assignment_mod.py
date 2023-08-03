"""
    Question: You are given a list of numbers obtained by rotating a sorted list an unknown number
    of times. You are also given a target number. Write a function to find the position of the
    target number within the rotated list. You can assume that all the numbers in the list are unique.

    Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 4.
"""

tests = [
    # A target is before the smallest number
    {
        'input': {
            'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14],
            'target': 29
        },
        'output': 2
    },
    # A target is after smallest number
    {
        'input': {
            'nums': [5, 6, 9, 0, 2, 3, 4],
            'target': 2
        },
        'output': 4
    },
    # A target is at the end
    {
        'input': {
            'nums': [10, 3, 5, 6],
            'target': 6
        },
        'output': 3
    },
    # the target is the smallest number
    {
        'input': {
            'nums': [9, 11, 3, 5, 6, 7],
            'target': 3
        },
        'output': 2
    },
    # A target is not in the list
    {
        'input': {
            'nums': [3, 5, 6, 7, 9, 11],
            'target': 1
        },
        'output': -1
    },
    # An empty list.
    {
        'input': {
            'nums': [],
            'target': 4
        },
        'output': -1
    },
    # A list containing just one element which is the target.
    {
        'input': {
            'nums': [4],
            'target': 4
        },
        'output': 0
    },
]


# [19, 25, 29, 3, 5, 6, 7, 9, 11, 14],
# 29
# [10, 3, 5, 6]
# 6
def find_element(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_num = nums[mid]
        if mid_num == target:
            return mid
        elif mid_num < nums[high] and mid_num < target <= nums[high]:
            low = mid + 1
        elif nums[high] < mid_num < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1   # Target not found


if __name__ == '__main__':
    for i, test in enumerate(tests):
        passed = find_element(**test['input']) == test['output']
        if passed:
            print(f"Test {i} Passed")
        else:
            print(f"Test {i} Failed")

    # print(find_element(**tests[2]['input']))
    # print(tests[2]['output'])
