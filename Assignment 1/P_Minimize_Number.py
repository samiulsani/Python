n = int(input())
arr = list(map(int, input().split()))
ans = 0
flag = False

while not flag:
    for i in range(n):
        if arr[i] % 2 != 0:
            flag = True
            break
        arr[i] //= 2
    if not flag:
        ans += 1

print(ans)
