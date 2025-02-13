num = int(input("Enter a number: "))
og_num = num
reversed = 0

while num > 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10
if og_num == reversed:
    print("Palindrome")
else:
    print("Not a Palindrome")