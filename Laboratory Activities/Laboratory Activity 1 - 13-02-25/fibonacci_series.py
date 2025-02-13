terms = int(input("Enter the number of terms: "))
first = 0
second = 1

if terms <=0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(first)
else:
    print(first, second, end=" ")
    for _ in range (terms-2):
        next = first+second
        print(next, end=" ")
        first = second
        second = next