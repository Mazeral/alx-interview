#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): A list of lists, where each inner list represents
        a box and contains the keys that can be found in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Get the number of boxes
    opened = [False] * n  # Initialize a list to keep track of opened boxes
    opened[0] = True  # The first box is already open
    keys = boxes[0]  # Get the keys in the first box

    while keys:
        """
        Loop until all keys have been found.
        """
        new_keys = []  # Initialize a list to store new keys
        for key in keys:
            """
            Iterate over the keys found so far.
            """
            if not opened[key]:
                """
                If the box corresponding to the key has not been opened yet.
                """
                new_keys.extend(boxes[key])  # Add the keys in the box to the
                # new_keys list
                opened[key] = True  # Mark the box as opened
        keys = new_keys  # Update the keys list with the new keys
    # Return True if all boxes have been opened, False otherwise
    return all(opened)
