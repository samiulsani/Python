n = int(input())
arr = list(map(int, input().split()))
freq_map = {}

for num in arr:
    if num in freq_map:
        freq_map[num] += 1
    else:
        freq_map[num] = 1
ans = 0
for key, value in freq_map.items():
    if value > key:
        ans += (value - key)
    elif value < key:
        ans += value

print(ans)
