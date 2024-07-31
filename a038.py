n = list(map(int, input().split()))

a = []
tmp = ""


if len(n) % 2 == 0: #偶數
    
    for i in range(len(n)-1):
        tmp = a[i]
        a[i] = a[len(n)]
        a[len(n)] = tmp

print(a)