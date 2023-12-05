n = int(input("введите число:"))
for i in range(n):
    if i * i % (10 ** len(str(i))) == i:
        print(i)