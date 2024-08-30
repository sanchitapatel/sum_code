'''n = int(input("Enter the total number of elements: "))
total_sum = 0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    total_sum += num
print(f"The sum of the {n} numbers is {total_sum}")
num = 11
# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")'''
# Python program to print Even Numbers in given range

start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num % 2 != 0:
        print(num)
