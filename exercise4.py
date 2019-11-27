number = input("Pick a number: ")
divisors = range(1, int(number))
result = []

for element in divisors:
    if int(number) % element == 0:
        result.append(element)
print(result)


