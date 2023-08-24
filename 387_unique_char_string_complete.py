# 387. First Unique Character in a String
def firstUniqChar(s):
    for i in range(0, len(s)):
        if s.count(s[i]) < 2 and s[i] not in s[i+1: ]: 
            return i
    else: return -1
    

input_s = "loveleetcode"
print(firstUniqChar(input_s))