def sum_of_nums(num):
    if num==1:
        return 1
    else:
        return num + sum_of_nums(num-1)

a = int(input())
print(sum_of_nums(a)) 