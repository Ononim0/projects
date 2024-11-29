from sumvols import*

def decod (cod, pas):
    finall = []
    finall1 = []
    finall2 = ""
    a = 0
    a1 = 0

    pas1 = list(pas)
    cod1 = list(cod)
    
    for i in cod1:
        if a1 >= len(pas1):
            a1 = 0

        secret1 = sumvols(cod1[a]) - int(pas1[a1])
        
        if secret1 > 0:
            finall = r_sumvols(secret1)
            finall1.append(finall)

        elif secret1 <= 0:
            finall = r_sumvols(secret1 + 63)
            finall1.append(finall)
        finall2 = finall2 + finall1[a]

        a = a + 1
        a1 = a1 + 1

    return(finall2)