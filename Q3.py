def getmatrix(rows,cols):
    A=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            m=int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(m)
        A.append(row)
    return A

rows=int(input("enter number of rows: "))
cols=rows
A=getmatrix(rows,cols)
print("matrix A=\n",A)
