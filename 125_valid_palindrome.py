class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_string = "".join([char_s.lower() for char_s in list(s) if char_s.isalnum() == True])
        if check_string == check_string[::-1]: return True
        return False
        
    
test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))