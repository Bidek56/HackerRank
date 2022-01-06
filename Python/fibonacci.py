def fibonacci(n):
    return n if n==1 or n==0 else fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))