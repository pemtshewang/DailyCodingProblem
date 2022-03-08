arr = list(map(int,input().split()))
find_max = max(arr)
for i in range(1,find_max+1):
    if i not in arr:
        print(i)
        break
else:
    print(find_max+1)
