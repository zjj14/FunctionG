def Functionthe(the):
    temp=the[0]

    theta=[]
    for element in the:
        a=(element - temp)/temp
        theta.append(a)
    return theta


