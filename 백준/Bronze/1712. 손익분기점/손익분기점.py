import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

profit = c - b

if profit <= 0:
    print(-1)
else:
    bep = (a // profit) + 1
    print(bep)