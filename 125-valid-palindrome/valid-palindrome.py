class Solution(object):
    def isPalindrome(self, s):
        parseado = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if parseado == parseado[::-1]:
            return True
        return False
        