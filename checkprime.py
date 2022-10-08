# PYTHON PROGRAM TO CHECK PRIME NUMBER OR NOT

num = int(input("Enter a number: "))

flag = 1
mid = num//2

for i in range(2,mid+1):
    if (num%i == 0):
        flag = 0
        break

if (flag == 1):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
