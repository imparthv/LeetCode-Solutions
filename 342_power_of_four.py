# 342. Power of Four
def isPowerOfFour(n):
    multiple = 1
    exponent = 0
    while multiple < n:
        multiple = 4 ** exponent
        exponent +=1 
    if multiple == n:return True
    else: return False

print("Enter the input number:")
inputNum = int(input())
print(isPowerOfFour(inputNum))