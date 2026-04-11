def countdown(num):
    if num == 0:
        print("Blast off!")
    else:
        countdown(num-1)
        print(num)
    
num = int(input())
countdown(num)