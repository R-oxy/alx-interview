#!/usr/bin/python3
""" lock Boxes"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened.

    Args:
        boxes (list of list): Locked boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    visited = set()
    visited.add(0)

    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)
