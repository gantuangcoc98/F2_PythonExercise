num = int(input("Please enter a number: "))

size = 0
min = 9
max = 0

while num :
    size += 1

    digit = num % 10

    if digit <= min :
        min = digit
    elif digit >= max :
        max = digit

    num = num // 10

print("Number of digits in the given number: " + str(size))
print("Smallest number is: " + str(min))
print("Highest number is: " + str(max))