nevek = [gabor, pista, marika, alexandra]
#result = 0
#for number in numbers:
#   result += number
#print(result)
max_name = nevek[0]
for nev in nevek:
    if len(nev) > len(max_name):
        max_name = nev
print(max_name)