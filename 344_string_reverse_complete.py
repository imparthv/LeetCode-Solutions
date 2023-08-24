# 344. Reverse String
def reverseString(s):
    #Leetcode solution accepts only s.reverse()
    print(s.reverse())

print("Enter string:")
s_string = str(input())
s_list = [s_char for s_char in s_string]
reverseString(s_list)