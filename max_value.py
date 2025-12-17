from itertools import product
k, m = map(int, input().split())
lists = []
for _ in range(k):
    data = list(map(int, input().split()))
    lists.append(data[1:])
max_value = 0
for combo in product(*lists):
    total = sum(x*x for x in combo) % m
    if total > max_value:
        max_value = total
print(max_value)