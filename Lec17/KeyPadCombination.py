
kmap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def kpc(ques,ans):
    if len(ques) == 0:
        print(ans)
    else:
        st = kmap[int(ques[0])]
        for i in st:
            kpc(ques[1:],ans+i)

kpc("23","")