# 58. Length of Last Word
def lengthOfLastWord(s):
    input_list = s.split()
    return len(input_list[-1])

print("Enter the statement:")
input_text = str(input())
last_length = lengthOfLastWord(input_text)
print(last_length)