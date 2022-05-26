"""
---The Fibonacci Sequence Version 2---
------By: Tommy H. Yeargin, Jr.-------
-------------May 25, 2022-------------
"""

# TARGET ANSWER...
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

sequence = [0, 1, 1]
[sequence.append(sequence[-1] + sequence[-2])for i in range(3,9)]
print(sequence)
