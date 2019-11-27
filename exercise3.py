a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Initial exercise")
for element in a:
    if element < 5:
        print(element)

print("\nExtra 1")
less_than_five = []

for element in a:
    if element < 5:
        less_than_five.append(element)
print(less_than_five)

print("\nExtra 3")
list_size = input("Type a number: ")
user_list = []
for element in a:
    if element < int(list_size):
        user_list.append(element)
print(user_list)



