def difference(list_):
    if len(list_)<3:
        return "range determination not possible"
    else:
        max_=max(list_)
        min_=min(list_)
        return max_-min_

list_=[5,3,8,1,0,4]
difference_=difference(list_)
print("range:",difference_)

