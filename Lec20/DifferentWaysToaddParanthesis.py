def isOp(op):
    return op == "+" or op == "-" or op == "*"

def operation(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    else:
        return a*b

def diff(exp):
    if "+" not in exp and "-" not in exp and "*" not in exp:
        return [int(exp)]
    else:
        rr = []
        for i in range(len(exp)):
            if isOp(exp[i]):
                r1 = diff(exp[:i])
                r2 = diff(exp[i+1:])

                for a in r1:
                    for b in r2:
                        rr.append(operation(a,b,exp[i]))
        return rr

def diffE(exp):
    if "+" not in exp and "-" not in exp and "*" not in exp:
        return [int(exp)]
    else:
        rr = []
        for i in range(len(exp)):
            if not exp[i].isdigit():
                r1 = diff(exp[:i])
                r2 = diff(exp[i+1:])

                for a in r1:
                    for b in r2:
                        rr.append(eval(str(a)+exp[i]+str(b)))
        return rr


print(diffE("2*3-4*5"))


