# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

sampleList = [8, 2, 3, 0, 7]


def SumOfNumbersInList(givenList):
    total = 0

    for x in givenList:
        total += x

    return total


print(SumOfNumbersInList(sampleList))
