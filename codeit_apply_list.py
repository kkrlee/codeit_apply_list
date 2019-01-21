numbers = []

i = 1
while i <= 10:
    numbers.append(i)
    i += 1
print(numbers)

i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 == 1:
        del numbers[i]
    i -= 1
print(numbers)


numbers.insert(0, 20)
print(numbers)

numbers.sort()
print(numbers)
