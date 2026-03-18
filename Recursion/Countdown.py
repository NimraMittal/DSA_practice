def countdown(num):
    if num == 0:
        print("Blast off!")
    else:
        print(num)
        countdown(num-1)
    
num = int(input())
countdown(num)