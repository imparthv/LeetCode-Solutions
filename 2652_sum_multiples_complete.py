# 2652. Sum Multiples
def sumOfMultiples(n):
    '''
    sum_num = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 :
            sum_num = i + sum_num
    return sum_num
    '''
    return sum([item for item in range(1, n+1) if item % 3 == 0 or item % 5 == 0 or item % 7 == 0])
    

print("Enter the number:")
input_num = int(input())
print(sumOfMultiples(input_num))