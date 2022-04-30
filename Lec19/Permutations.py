def pm1(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(len(ques)):
            nq = ques[:i]+ques[i+1:]
            pm1(nq,ans+ques[i])

def pm2(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(len(ans)+1):
            na = ans[:i] + ques[0] + ans[i:]
            pm2(ques[1:],na)



def tpm(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(len(ques)):
            if ques[i] not in ques[i+1:]:
                nq = ques[:i]+ques[i+1:]
                tpm(nq,ans+ques[i])


tpm("abca","")
