# 728. Self Dividing Numbers
def selfDividingNumbers(left, right):
    '''
    self_divide_list = []
    for item in range(left, right + 1):
        if item > 0 and item  < 9:
            self_divide_list.append(item)
        else:
           if str(0) not in str(item):
            i = 0
            for digit in str(item):
                if item % int(digit) == 0:
                    i +=1
            if i == len(str(item)):
                self_divide_list.append(item)
    return self_divide_list
    '''
    
    

print("Enter the extremes:")
right_extreme = int(input())
left_extreme = int(input())
num_list = selfDividingNumbers(right_extreme, left_extreme)
print(num_list)