#week01-2.py 學習計畫 Array/string 第一題
#1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans ="" #答案塞在ans裡面
        N1,N2 = len(word1), len(word2)
        i, j = 0, 0 #word1[i] VS. word[j]
        while  i<N1 or  i<N2: #只要任一個還有剩
            if  i<N1:ans += word1[i]  #沒用完
            if  j<N2:ans += word2[j]  #沒用完
            i, j = i+1, j+1 #都換下一位
        return ans #答案