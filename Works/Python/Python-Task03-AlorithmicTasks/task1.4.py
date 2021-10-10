# Write a function called lastElement. This function takes one parameter (a list)
# and returns the last value in the list. It should return None if the list is empty.
# Example Output
# lastElement([1,2,3]) # 3
# lastElement([]) # None

def lastElement(givenList):
    if givenList:
        return givenList[-1]
    # else:
    #     None


sampleList0 = [1, 2, 3, 5, 8, 9]
sampleList1 = []
print(lastElement(sampleList0))
print(lastElement(sampleList1))
