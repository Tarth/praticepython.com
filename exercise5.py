import random

a = range(1, round(random.random() * 50))
b = range(1, round(random.random() * 50))
result = []

for element_a in a:
    for element_b in b:
        if element_a == element_b:
            if result.count(element_b) == 0:
                result.append(element_b)
print("List a: " + str(a))
print("List b: " + str(b))
print(result)


def random_list(list_max):
    list = []
    list.append(1)
    for element
round(random.random() * 10)



