size = int(input())
n = int(input())
arr = list(map(int,input()))
count = 0
empty_left = False
empty_right = True
for i in range(size):
    if arr[i]==0:
        empty_left = (i == 0 or arr[i-1]==0)
        empty_right = (i == size-1 or arr[i+1]==0)
    if empty_left and empty_right:
        arr[i]=1
        count += 1
        if count>=n:
            break
if count >= n:
    print("true")
else:
    print("false")