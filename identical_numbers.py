while True:
    number = input("Enter the number:")
    identical_number = False
    length = len(number)
    for i in range(length):
        for j in range(i + 1, length):
            if number[i] == number[j]:
                identical_number = True
                break
    if identical_number:
        print("Yes")
    else:
        print("No")