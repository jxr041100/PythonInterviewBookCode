def addBinary(a:str, b:str) -> str:
    len_a = len(a) #字符串a的长度
    len_b = len(b) #字符串b的长度
    # 取两者最长的
    max_length = max(len_a, len_b)
    carry=0 #进位标志
    new_str=[]
    for i in range (-1,-max_length-1,-1): #从右往左遍历字符串
        element_a = 0
        element_b = 0
        if abs(i) <= abs(len_a): #取字符串a的值
            element_a = a[i]

        if abs(i) <= abs(len_b): #取字符串b的值
            element_b = b[i]
        # 字符串a/b的值相加，再加上进位标志
        add = int(element_a) + int(element_b) + int(carry)
        value = add %2 #当前位置的值
        carry = add //2 #进位
        new_str.insert(0,str(value)) #将新产生的值插入新的字符串首位。
    if carry !=0:#最后不要忘记进位标志不为零的情况
        new_str.insert(0, str(carry))
    return ''.join(new_str)
    #时间复杂度为O(N)，空间复杂度为O(1)
