# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

sampleList = [8, 2, 3, -1, 7]


def ProductOfNumbersInList(givenList):
    product = 1
    for x in givenList:
        product = x * product

    return product


print(ProductOfNumbersInList(sampleList))
