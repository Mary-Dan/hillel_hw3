# 1
sum = 0
i = int(input("введите число:"))
while i != 0:
    sum += i
    i = int(input())
print(sum)

#2
sum = 0
count = 0
while True:
    num = int(input("Enter the number): "))
    if num == 0:
        if count == 0:
            print("ok")
        else:
            result = sum / count
            print(result)
        break
    sum += num
    count += 1

# 3
numbers = []
while True:
   number = int(input())
   if number == 0:
       break
   numbers.append(number)
print(max(numbers), min(numbers))

#4
even_count = 0
odd_count = 0
while True:
    num = int(input("Enter the number): "))
    if num == 0:
        print(even_count)
        print(odd_count)
        break
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1