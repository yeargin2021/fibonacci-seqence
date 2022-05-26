"""
---The Fibonacci Sequence---
-By: Tommy H. Yeargin, Jr.--
--------May 25, 2022--------
"""

# TARGET ANSWER...
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

sequence = [0, 1, 1]

number = sequence[-1]

def populateList():
    sequence.append(number)

for i in range(3,9):
    number = sequence[-1] + sequence[-2]
    populateList()

print(sequence)
