t = int(input())

for _ in range(t):
    n, a, b, c = map(int, input().split())

    if a + b + c > n:
        print(-1)
        continue

    need = {'R': a, 'G': b, 'B': c}
    res = []
    prev = ''

    for _ in range(n):
        placed = False

        colors = sorted(['R','G','B'], key=lambda x: -need[x])

        for color in colors:
            if need[color] > 0 and color != prev:
                res.append(color)
                need[color] -= 1
                prev = color
                placed = True
                break

        if not placed:
            if sum(need.values()) == 0:
                for color in ['R','G','B']:
                    if color != prev:
                        res.append(color)
                        prev = color
                        placed = True
                        break

        if not placed:
            print(-1)
            break
    else:
        print(''.join(res))
