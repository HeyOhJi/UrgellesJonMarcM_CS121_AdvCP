num = int(input("Enter a number: "))

if num<2:
    print(f"{num} is not a perfect number.")
else:
    sumdivisor = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sumdivisor += divisor
    if sumdivisor == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")