
# https://www.hackerrank.com/challenges/repeated-string

s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))