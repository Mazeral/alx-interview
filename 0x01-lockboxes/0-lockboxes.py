#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list contains keys
        to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a queue with the first box
    queue = [0]
    # Add the first box to the visited set
    visited.add(0)

    # Continue the BFS traversal until the queue is empty
    while queue:
        # Dequeue the next box
        box = queue.pop(0)
        # Iterate over the keys in the current box
        for key in boxes[box]:
            # If the key has not been visited before
            if key not in visited:
                # Add the key to the visited set
                visited.add(key)
                # If the key is within the bounds of the boxes list
                if key < len(boxes):
                    # Add the key to the queue
                    queue.append(key)

    # Return True if all boxes have been visited, False otherwise
    return len(visited) == len(boxes)
