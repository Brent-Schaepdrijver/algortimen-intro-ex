#The row of Lucas starts with 2 and 1 and each subsequent number is the sum of the two numbers preceding the number.
#What is the sum of all odd numbers in the row of Lucas smaller than 4 000 000?

#Hint the row of Lucas starts with: 2, 1, 3, 4, 7, 11, ...

Number1 = 2
Number2 = 1
Number3 = 30
list = []
totalnumber = 0

for number in range(0,4000001):
    number = Number1 + Number2
    Number1 = Number2
    Number2 = number
    
    if (number % 2 == 0): # Alle even getallen
        list.append(int(number))
        totalnumber = sum(list)
print (totalnumber)