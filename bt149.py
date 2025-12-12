def xet(diem):
    maxdiem=0
    
    for i in range(len(diem)):
        mangtest={}
        x1=diem[i][0]
        y1=diem[i][1]
        for j in range(len(diem)):
            x2=diem[j][0]
            y2=diem[j][1]

            if x1 == x2 and y1 == y2:
                continue

            if x1!=x2:
                hesogoc=(y1-y2)/(x1-x2)
            else:
                hesogoc='ngang'
            mangtest[hesogoc] = mangtest.get(hesogoc, 0) + 1
            #print(mangtest)

        maxdiem=max(maxdiem,max(mangtest.values())+1)

    return maxdiem



if __name__ == "__main__":
    diem= [[1,1],[2,2],[3,3],[3,4],[5,6],[7,7]]
    print(xet(diem))