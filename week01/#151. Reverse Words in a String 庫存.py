#151. Reverse Words in a String
#將word裡的word 倒邊來放
#151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split() #用空白 把字斷成很多字
        ans = []
        for i in range(len(a)-1, -1, -1): #倒過來的迴圈
            ans.append(a[i]) #把自塞入ans中
        return ' '.join(ans) #用空格隔開  

        