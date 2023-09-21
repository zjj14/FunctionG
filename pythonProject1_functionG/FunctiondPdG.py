def FunctiondPdG(p,G):
    dPdG=[]
    dPdG.append(0)
    for z in range(len(p)-1):
        a=(p[z]-p[z+1])/(G[z+1]-G[z])
        dPdG.append(a)
    return dPdG
