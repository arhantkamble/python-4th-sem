#program for the pattern
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()

# Program to print Fibonacci sequence up to nth number
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

num = int(input("Enter the number of terms: "))
fibonacci(num)