def countpairs(list_,pairsum):
    pairs=0
    for i in range(len(list_)):
        for j in range(i+1,len(list_)):
            if list_[i]+list_[j]==pairsum:
                pairs+=1
    return pairs

list_=[2,7,4,1,3,6]
pairsum=10
count=countpairs(list_,pairsum)
print("No of pairs with sum =",pairsum,"is",count)
