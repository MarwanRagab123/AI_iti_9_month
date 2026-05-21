
t = int(input())

for _ in range(t):
    a , b , c = map(int, input().split())
    new_cost = (c * b * b + a * a - 1) // (a * a)
    price = ((new_cost + 9) // 10) * 10

    print(price)