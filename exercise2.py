number = input("Type in a number: ")
num = input("Your check number: ")
check = input("Number to divide by: ")

if int(number) % 4 == 0:
    print(number + " is a multiple of 4")
elif int(number) % 2 == 0:
    print(number + " is even")
else:
    print(number + " is odd")

result = int(num) / int(check)

if result % 2 == 0:
    print("The result is even")
else:
    print("The result is odd")
