#week03-1.py
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1,n2 = len(str1), len(str2) #字串長度
        n = gcd(n1, n2) #最大公英數
        ans = str1[:n] #字串的前面N字母

        if ans*(n1//n) != str1: return "" #不符合 就失敗
        if ans*(n2//n) != str2: return ""

        return ans
        