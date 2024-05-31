class Solution(object):
    def duplicateNumbersXOR(self, nums):
        table = {} #大括號=字典:[num]對應的次數
        for num in nums: #每個數字倫一次
            if num in table: #出現過的話
                table[num] += 1 #次數+1
            else:
                table[num] =1 #第1次出現
        #print(table) #答案還沒算出來
        
        ans = 0
        for num in table: #把table裡全部的數字倫一遍
            if table[num]==2: #如果數字剛好出現2次
                ans = ans^num #把答案照題目要求 XOR混起來
        return ans