def sum_of_arr(arr):
    if len(arr)==0:
        return 0
    else:
        firsr_element = arr[0]
        rest_of_the_list = arr[1:]

        return firsr_element + sum_of_arr(rest_of_the_list)
    
arr = [2,4,6,5,8,7]
print(sum_of_arr(arr))
