# 326. Power of Three
def isPowerOfThree(n):
    multiple = 1
    exponent = 0
    while multiple < n:
        multiple = 3 ** exponent
        exponent +=1 
    if multiple == n:return True
    else: return False

inputNum = int(input())
print(isPowerOfThree(inputNum))