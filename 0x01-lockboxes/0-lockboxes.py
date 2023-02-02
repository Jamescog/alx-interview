#!/usr/bin/python3
"""Implementation of lockboxes"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    param:
        boxes(List): A list of lists, where each box is numbered
        sequentially from 0 to n - 1 and each
        box may contain keys to the other boxes.
    return: True if all boxes can be opened, else False.
    """


    opened = set([0])
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)

