n = int(input())

for i in range(n):
    p = list(map(int, input().split()))

    if p[2] - p[1] == p[1] - p[0]:
        a = p[3] + (p[1] - p[0])
    else:
        a = p[3] * (p[1] / p[0])
    
    print(p[0], p[1], p[2], p[3], int(a))