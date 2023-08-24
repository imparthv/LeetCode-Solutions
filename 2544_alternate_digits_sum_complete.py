# 2544. Alternating Digit Sum
def alternateDigitSum(n):
    '''
    sum = i = 0
    n = str(n)
    while i != len(n):
        if i % 2 == 0: sum += int(n[i])
        else: sum -= int(n[i])
        i+=1
    return sum
    '''

print("Enter the digit:")
digit = int(input())
print(alternateDigitSum(digit))