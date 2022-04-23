

def ss1(st):
    if len(st) == 0:
        return [""]
    else:
        rr = ss1(st[1:])
        ans = []
        ch = st[0]
        for i in rr:
            ans.append(ch+i)
            ans.append(i)
            # ans.append(str(ord(ch))+i)
        
        return ans

def ss2(ques,ans):
    if len(ques) == 0:
        print(ans)
        return 1
    else:
        c = 0
        c += ss2(ques[1:],ans)
        c += ss2(ques[1:],ans+ques[0])
        return c
        
def Asciiss(ques,ans):
    if len(ques) == 0:
        print(ans)
        return 1
    else:
        c = 0
        c += Asciiss(ques[1:],ans)
        c += Asciiss(ques[1:],ans+ques[0])
        c += Asciiss(ques[1:],ans+str(ord(ques[0])))
        return c


print(Asciiss("bc",""))
# print(type(ord('c')))



