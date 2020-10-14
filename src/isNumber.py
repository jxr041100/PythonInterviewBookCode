
class IsNumber:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        ls = s.split('e')
        if len(ls) == 1: #没有e
            return self.decide_num(ls[0])
        elif len(ls) == 2: #有e,分成两个部分，
            return self.decide_num(ls[0]) and self.decide_pow(ls[1])
        else:
            return False

    def decide_num(self,s):
        if not s:
            return False
        if s[0] in ['+', '-']:
            s = s[1:]
        ls = s.split('.')
        if len(ls) == 1: #没有小数点，确保数字有效
            return ls[0].isnumeric()
        elif len(ls) == 2: #有小数点
            if not ls[0] and ls[1].isnumeric(): #小数点前面为空
                return True
            elif not ls[1] and ls[0].isnumeric():#小数点后面为空
                return True
            else:
                return ls[0].isnumeric() and ls[1].isnumeric() #小数点前后部分都是有效数字

    def decide_pow(self, s):#记住幂中只有正负号+数字了，不可能出现小数点。
        if not s:
            return False
        if s[0] in ['+', '-']:
            s = s[1:]
        return s.isnumeric()