# All thanks to Jovian
"""
    QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in
    decreasing order, and lays them out face down in a sequence on a table. She challenges
    Bob to pick out the card containing a given number by turning over as few cards as
    possible. Write a function to help Bob locate the card.
"""

#  Test cases

tests = [
    # query occurs in the middle
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        },
        'output': 3
    },
    # query is the first element
    {
        'input': {
            'cards': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
    },
    # query is the last element
    {
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    },
    # cards contains just one element, query
    {
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0
    },
    # cards does not contain query
    {
        'input': {
            'cards': [9, 7, 5, 2, -9],
            'query': 4
        },
        'output': -1
    },
    # cards is empty
    {
        'input': {
            'cards': [],
            'query': 7
        },
        'output': -1
    },
    # numbers can repeat in cards
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    },
    # query occurs multiple times
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6
        },
        'output': 2
    }
]


def locate_card(cards, query):
    # Bruteforce
    # Time complexity: Best case O(1), Worst case O(N)
    # Space complexity: O(1)
    # for i, card in enumerate(cards):
    #     if card == query:
    #         return i
    # return -1

    # implement the right technique to overcome inefficiency since the card is sorted
    # Time complexity: Best case O(1), Worst case O(logN)
    # Space complexity: O(1)
    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_card = cards[mid]
        if mid_card == query:
            if mid - 1 >= 0 and cards[mid - 1] == query:
                high = mid - 1  # left
            else:
                return mid      # found
        elif mid_card < query:
            high = mid - 1  # left
        else:
            low = mid + 1  # right
    return -1


if __name__ == '__main__':
    for i, test in enumerate(tests):
        passed = locate_card(**test['input']) == test['output']
        if passed:
            print(f"Test {i} Passed")
        else:
            print(f"Test {i} Failed")
