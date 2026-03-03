arr = list(map(int,input().split()))

if len(arr) == 0:
    print(0)
else:
    current_sum = 0
    max_sum = 0
    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum+arr[i])
        max_sum = max(max_sum, current_sum)
    print(max_sum)