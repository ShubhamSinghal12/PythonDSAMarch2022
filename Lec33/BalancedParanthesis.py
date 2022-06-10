# s = "(([{}]()[]))"
s = "({)}"

def isBalanced(s):
    st = []
    for i in s:
        # print(i,st)
        if i in "({[":
            st.append(i)
        else:
            if len(st) == 0:
                return False
            if i == ")" and (st[-1] == "{" or st[-1] == "[") :
                return False
            elif i == "}" and (st[-1] == "[" or st[-1] == "(") :
                return False
            elif i == "]" and (st[-1] == "(" or st[-1] == "{") :
                return False
            
            st.pop()
    
    if len(st) == 0:
        return True
    else:
        return False        



def isBalanced2(s):
    st = []
    for i in s:
        # print(i,st)
        if i  == "(":
            st.append(')')
        elif i == "{":
            st.append("}")
        elif i == "[":
            st.append("]")
        else:
            if len(st) == 0:
                return False
            x = st.pop()
            if i != x:
                return False
    
    if len(st) == 0:
        return True
    else:
        return False       



print(isBalanced2(s))