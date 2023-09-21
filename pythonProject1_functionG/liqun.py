def deleteliqun(data,threshold):

    output1=[]

    for index in range(len(data)-1):
        if abs(data[index+1]-data[index])>threshold:
            output1.append(data[index]*0.5+data[index+1]*0.5)
        else:
            output1.append(data[index])
    return output1
