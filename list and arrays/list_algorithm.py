#Create an algorithm to find the lowest value in a list
num = [45,67,23,89,10,57,98]
minval = num[0]
for i in num:
    if (i<minval):
        minval = i
print('Lowest value:', minval)   #Lowest value: 10

#Create an algorithm to find the highest value in a list
num = [45,67,23,89,10,57,98]
minval = num[0]
for i in num:
    if (i<minval):
        i = minval
print('highest value:', i) #highest value: 98

