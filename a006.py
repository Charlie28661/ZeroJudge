import math

a, b, c = map(int, input().split())

d = b**2 - 4 * a * c

if d > 0:
    x1 = int((-b + math.sqrt(d)) /(2 * a))
    x2 = int((-b - math.sqrt(d)) /(2 * a))
    print(f"Two different roots x1={x1} , x2={x2}")
elif d == 0:
    x = int((-b + math.sqrt(d)) /(2 * a))
    print(f"Two same roots x={x}")
else:
    print("No real root")