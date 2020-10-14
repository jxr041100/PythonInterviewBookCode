from collections import deque
class MinRemoveToMakeValid:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = deque()
        for i, ch in enumerate(s):
            if ch=='(':
                stk.append(i)
            elif ch == ')':
                # 如果前面一个是（，则出栈
                if  stk and s[stk[-1]]=='(':
                    stk.pop()
                else:
                    stk.append(i)
        res=""
        #现在堆栈里面留下的就是多余的括号，下面就是需要删除掉。
        for i in range(len(s)):
            if stk and i==stk[0]:
                stk.popleft()
            else:
                res+=s[i]
        return res