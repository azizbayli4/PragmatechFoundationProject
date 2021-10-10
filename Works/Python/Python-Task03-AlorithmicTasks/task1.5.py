# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def evenNumsInList(givenList):
    for x in givenList:
        if x % 2 == 0:
            print(x, end=",")


sampleLsit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenNumsInList(sampleLsit)
