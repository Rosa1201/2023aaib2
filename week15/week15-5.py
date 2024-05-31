class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        N = len(s)
        j = 0 #尾巴
        for i in range(N): #頭是i
            maxCost -= abs(ord(s[i])-ord(t[i])) #毛毛蟲頭i 吃葉子
            while maxCost < 0: #預算不夠變負
                maxCost += abs(ord(s[j])- ord(t[j]))
                j += 1 #尾巴j往右縮
            ans = max(ans,i-j+1)
        return ans
