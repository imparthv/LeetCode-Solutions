# 231. Power of Two
def isPowerOfTwo(n):
    multiple = 1
    exponent = 0
    while multiple < n:
        multiple = 2 ** exponent
        exponent +=1 
    if multiple == n:return True
    else: return False

print("Enter the integer:")
target = int(input())
print(isPowerOfTwo(target))