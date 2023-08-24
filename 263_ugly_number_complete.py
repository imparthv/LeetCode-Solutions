# 263. Ugly Number
def isUgly(n):
    if n == 1: return True 
    elif n == 0: return False
    else:
        if n % 2 == 0 :
            n = n / 2
            return isUgly(n)
        elif n % 3 == 0 :
            n = n / 3
            return isUgly(n)
        elif n % 5 == 0 :
            n = n / 5
            return isUgly(n)
        else: return False

print("Enter the number:")
target = int(input())
print(isUgly(target))