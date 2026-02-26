#week01-1.py
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        n = int (s,2) #把字串 s 當二進為整數變成n
        while n > 1: #目標N最後變成1
            if n%2==0: n = n//2 #是偶數的話 //2
            else: n = n + 1 #否則+1
            ans += 1 #又多做了一部
        return ans #總共做幾部