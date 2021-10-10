# Write a function called returnDay. This function takes in one parameter ( a number from 1-7)
# and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or
# greater
# than 7, the function should return None.
# Expected output
# returnDay(1) --> Sunday

def returnDay(a):
    daysOfWeek = ['Sunday', 'Monday', 'Tuersday',
                  'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for i in range(len(daysOfWeek)):
        dayIndex = i
        if dayIndex+1 == a:
            return daysOfWeek[dayIndex]
    else:
        return None


print(returnDay(5))


# weekDays = {
#     1: 'Sunday',
#     2: 'Monday',
#     3: 'Tuesday',
#     4: 'Wednesday',
#     5: 'Thursday',
#     6: 'Friday',
#     7: 'Saturday',
# }


# def returnDay(num):

#     if weekDays[num]:
#         return weekDays[num]
#     else:
#         return None


# print(returnDay(1))
