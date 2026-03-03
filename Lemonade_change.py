n = int(input())
bills = list(map(int,input().split()))

five = 0
ten = 0
possible = True

for bill in bills:
    if bill == 5:
        five += 1
    elif bill == 10:
        if five>0:
            ten += 1
            five -= 1
        else:
            possible = False
            break
    elif bill == 20:
        if ten >= 1 and five >= 1:
            ten -= 1
            five -= 0
        elif five >= 3:
            five -= 3
        else :
            possible = False
            break

if possible:
    print("true")
else:
    print("false")
