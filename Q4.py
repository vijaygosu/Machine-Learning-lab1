def max_occur(string):
    count={}
    for i in string:
            count[i]=count.get(i,0)+1

    max_char=max(count,key=count.get)
    max_count=count[max_char]

    return max_char, max_count

string="hippopotamus"
char,count= max_occur(string)
print("the most occurring character is ",char," with count",count)
