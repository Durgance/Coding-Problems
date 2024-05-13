class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        flag = False
        break_flag = False
        counter = 0
        counter_plus = 0
        for i in range(len(s)):
            
            if (break_flag == True and (s[i]=="-" or s[i]=="+" or s[i]==" " or not s[i].isnumeric)) or counter >1:
                break
            if s[i]==" ":
                if counter_plus == 1:
                    break
                continue
            if s[i] == "+":
                counter_plus = 1
                counter += 1
                continue
            if s[i] == "-":
                counter += 1
                flag = True
                continue
            if not s[i].isnumeric():
                break
            ans += s[i]
            break_flag = True

        print(ans)
        if len(ans)==0:
            return 0
        # if ans[0] == "0":
        #     return 0
        if flag == True:
            ans = -1*int(ans)
        else:
            ans = int(ans)
        if pow(-2,31) <= ans and ans <= pow(2,31)-1:
            return ans
        if ans<0:
            return pow(-2,31)
        return pow(2,31)-1