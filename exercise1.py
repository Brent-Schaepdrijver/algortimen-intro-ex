Number1 = 0
Number2 = 10001
list = []
numbers = 0
for number in range(Number1, Number2):
    if (number%7==0) or (number%9==0):
        list.append(int(number))
        numbers = sum(list)
print (numbers)
