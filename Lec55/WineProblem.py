def wine(price,si,ei):
    y = len(price)-(ei-si)
    if si == ei:
        return price[si]*y
    else:
        fc = price[si]*y + wine(price,si+1,ei)
        lc = price[ei]*y + wine(price,si,ei-1)

        return max(fc,lc)




pr = [2,3,5,1,4]
print(wine(pr,0,len(pr)-1))