
def findwh(P):
    length_p = len(P)
    gen=0
    water_hammer=[]
    for i in range(1, length_p - 1):
        if P[i]>= P[i-1] and P[i] >= P[i+1]:
            gen=i
    if gen!=0:
        water_hammer=P[:gen]
    return water_hammer
