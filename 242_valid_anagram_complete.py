# 242. Valid Anagram
def isAnagram(s, t):
   s_list = sorted([s_items for s_items in s])
   t_list = sorted([t_items for t_items in t])
   if s_list == t_list: return True
   else: return False

print("Enter inputs:")
s_string = str(input())
t_string = str(input())
print(isAnagram(s_string, t_string))