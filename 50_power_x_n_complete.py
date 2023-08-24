# 50. Pow(x, n)
def myPow(x, n):
    return float(x ** n)

print("Enter base and exponent:")
base_number = float(input())
exponent_number =  int(input()) 
print(myPow(base_number, exponent_number))