def container(g1):
    ra=0
    i=0
    j=len(g1)-1
    
    while True:
        tam=(j-i)*min(g1[i],g1[j])
        if tam>ra:
            ra=tam
        
        if g1[i]>g1[j]:
            j-=1
        else:
            i+=1
        if i==j:
           break
    return ra
if __name__ == "__main__":
    g1 = [1,1,2,1,2,1,1,1]
    g2 =[1,8,6,2,5,4,8,3,7]


    print(container(g1))
    print(container(g2))