# 9. Palindrome Number
# Optimised with speed
def isPalindrome(x):
    if str(x) == str(x)[::-1]: return True
    return False

print("Enter the number:")
input_num = int(input())
output = isPalindrome(input_num)
print(output)

