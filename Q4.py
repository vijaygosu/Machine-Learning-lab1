def max_occur(string):
    count
    for i in string:
            count[i]=count.get(char,0)+1

    max_char=max(char_count,key=char_count.get)
    max_count=char_count[max_char]

    return max_char, max_count

string="hippopotamus"
char,count= max_occur(string)
print("the most occurring character is ",char," with count",count)
