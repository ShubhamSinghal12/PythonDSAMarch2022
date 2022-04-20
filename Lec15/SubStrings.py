from audioop import reverse


st = "abcde"

def subString(st):
    for i in range(len(st)+1):
        for j in range(i+1,len(st)):
            print(st[i:j],end = " ")


subString(st)
print()


def reverseString(st):
    return st[::-1]

def reverseString2(st):
    ans = ""
    
    for i in range(len(st)-1,-1,-1):
        ans += st[i]
    
    return ans

print(reverseString2(st))

def isPalindrome1(st):
    return st == st[::-1]

def isPalindrome2(st):
    si = 0
    ei = len(st)-1

    while si < ei:
        if st[si] != st[ei]:
            return False
        else:
            si += 1
            ei -= 1

    return True 

print(isPalindrome2("nitin"))



def countPalindromicSubString(st):
    count  = 0
    for i in range(len(st)):
        for j in range(i+1,len(st)+1):
            if isPalindrome1(st[i:j]):
                count += 1
    
    print(count)


countPalindromicSubString("nitin")

def reverseWord(st):
    words = st.split()
    ans = ""
    for i in range(len(words)-1,0,-1):
        ans = ans + words[i]+" "
    
    ans += words[0]
    
    print(ans)

reverseWord("The sky is Blue")

