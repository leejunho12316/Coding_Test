N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=False)

result = 0
for i in range(1, len(arr) + 1):
    result += sum(arr[:i])

print(result)

