from sumvols import*

def cod (secret, cod):

        list1 = []
        secret1 = []
        finall1 = []
        finall = []
        finall2 = ""
        a1 = 0
        a = 0

        list1 = list(secret)
        cod1 = list(cod)
    
        for i in list1:
            if a1 >= len(cod1):
                 a1 = 0
 
            secret1 = sumvols(list1[a]) + int(cod1[a1])

            if secret1 <= 63:
                finall = r_sumvols(secret1)
                finall1.append(finall)


            elif secret1 > 63:
                finall = r_sumvols(secret1 - 63)
                finall1.append(finall)
             
            finall2 = finall2 + finall1[a]

            a1 = a1 +1
            a = a + 1   
            
        return(finall2)