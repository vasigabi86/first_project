numbers = [10, 24, 21, 25, 2, 234, 64, 534]
result = 0
#for number in numbers:
#   result += number
#print(result)
min = numbers[0]

for number in numbers:
    if number < min:
        min = number

print('A legkisebb szám a listában: ', min)


