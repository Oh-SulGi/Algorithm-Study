import sys
input = sys.stdin.readline

a, b = map(int, input().split())

result = a * ((100 - b) / 100)

if result >= 100:
    print(0)
else:
    print(1)