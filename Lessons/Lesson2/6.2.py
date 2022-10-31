numbers = "0139412831055230677798"
numbers_dict = {}
for i in range(10):
    numbers_dict[i] = numbers.count(str(i))
print(numbers_dict)