#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True  # First box is unlocked by default
    
    keys = boxes[0]  # Start with keys from the first box
    for box in keys:
        if box < num_boxes and not unlocked[box]:
            unlocked[box] = True
            keys.extend(boxes[box])
    
    return all(unlocked)
