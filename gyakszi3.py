a, b = 7, 1
while b <= 20:
    b = b + 1
    if (a * b) % 3 == 0:
        print(a * b, "*")
    else:
        print(a * b)
