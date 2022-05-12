def tpm(ques,ans):
    if len(ques) == 0:
        # print(ans)
        return 1
    else:
        c = 0
        if len(ans) != 0:
            # print(ans)
            c += 1
        for i in range(len(ques)):
            if ques[i] not in ques[i+1:]:
                nq = ques[:i]+ques[i+1:]
                c += tpm(nq,ans+ques[i])
        return c


print(tpm("AAB",""))