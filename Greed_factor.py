child_count = int(input())
greed_factor = list(map(int,input().split()))
cookie_count = int(input())
cookie_size = list(map(int,input().split()))

greed_factor.sort()
cookie_size.sort()

i = 0
j = 0

satisfied = 0

while i < child_count and j < cookie_count:
    if cookie_size[j]>=greed_factor[i]:
        satisfied += 1
        i += 1
    j += 1

print(satisfied)