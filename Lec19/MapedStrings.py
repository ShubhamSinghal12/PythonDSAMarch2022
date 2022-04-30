def mps(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        i = int(ques[0])
        mps(ques[1:],ans+chr(i+64))

        if len(ques) >= 2:
            i = int(ques[0:2])
            if i <= 26:
                mps(ques[2:],ans+chr(i+64))

mps("127","")

