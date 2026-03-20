def digit_sum(num):
    if num < 10:
        return num
    else:
        sum = num % 10
        return sum + digit_sum(num//10)
    
num = 44987
print(digit_sum(num))