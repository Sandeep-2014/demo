number = int(input("enter the number: "))
sum = 0
while number != 0:
        fact = number % 10
        sum += fact
        number = number // 10
print(sum)
