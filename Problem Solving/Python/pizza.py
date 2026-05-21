import math

t = int(input())

for _ in range(t):
    a , b , c = map(int, input().split())
    r_balance = c * ((b*b)/(a*a))
    price =math.ceil(r_balance/10) * 10

    print(price)