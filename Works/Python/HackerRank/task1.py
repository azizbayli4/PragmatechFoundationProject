def recurrence(n):
    if(n == 0):
        print(0, end = ",")
        # return 0
    elif(n == 1):
        print(1, end = ",")
        # return 1
    else:
        result = (3*recurrence(n-1)) - (2*recurrence(n-2))
        print(result, end = ",")
        # return result

recurrence(5)