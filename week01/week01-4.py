#week01-4.py 學習計畫  array/string 第三題
#1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        best = max(candies) #目前小朋友 最多有幾個糖?
        for candy in candies: #逐一檢查 如果把extraCandies給小朋友
            if candy + extraCandies >= best: ans.append(True) #加起來後 >= 目前小朋友就true
            else: ans.append(False) #否則flase
        return ans 