def Maxmuim(the, p):
    length_p = len(p)
    maxvalue = 0
    the_max = 0
    cixu=0
    for i in range(1, length_p-1):
        if p[i] >= p[i-1] and p[i] >= p[i+1] and i<length_p/2:
            maxvalue = p[i]
            the_max = the[i]
            cixu=i
    jida = [the_max, maxvalue,cixu]
    return jida
