def calculate_slope(G,P, i):
    slope = (P[i + 5] - P[i]) / (G[i+5]-G[i])
    return slope
def update_values(G1,P, i):
    slope = calculate_slope(G1,P, i)
    for j in range(i):
        P[j]=P[i]-slope*(G1[i]-G1[j])

    return P
