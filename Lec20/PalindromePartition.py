def pp(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        for i in range(1,len(ques)+1):
            part = ques[:i]
            if part == part[::-1]:
                pp(ques[i:],ans+part+" ")

pp("nitin","")