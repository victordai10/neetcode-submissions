class Solution:
    def isPalindrome(self, s: str) -> bool:
        # helper function to determine if c is alphanumeric; same as isalnum()
        
        
        # two pointer
        # forward pass:
        forward = ""
        for c in s:
            if self.alphaNum(c):
                forward += c.lower()
            
        # backward pass:
        backward = ""
        for i in range(len(s) - 1, -1, -1):
            if self.alphaNum(s[i]):
                backward += s[i].lower()
        
        return forward == backward

    def alphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )