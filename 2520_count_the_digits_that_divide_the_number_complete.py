# 2520. Count the Digits That Divide a Number
# Optimised
def countDigits(num):
    '''
    count = 0
    for item in str(num):
        if num % int(item) == 0: count += 1
    return count
    '''
    return len([item for item in str(num) if num % int(item) == 0])
    

print("Enter the number:")
input_num = int(input())
print(countDigits(input_num))