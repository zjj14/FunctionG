import math
def FunctionG(the):
    G=[]
    for element in the:
        a=16*((1+element)**(3/2)-element**(3/2)-1)/(3*math.pi)
        G.append(a)
    return G
