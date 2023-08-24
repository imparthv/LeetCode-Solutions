# 509. Fibonacci Number
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("Enter the number:")
target_n = int(input())
fib_seq = fib(target_n)
print(fib_seq)