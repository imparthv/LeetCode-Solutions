# 415. Add Strings
def addStrings(num1, num2):
    num1= int(num1)
    num2 = int(num2)
    return str(num1 +num2)

print("Enter the input:")
num_string1 = input()
nums_string2 = input()
added_strings = addStrings(num_string1, nums_string2)
print(added_strings)
print(type(added_strings))