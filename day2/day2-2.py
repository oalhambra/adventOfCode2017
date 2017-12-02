

f = open("input.txt","r")
data=f.read()
data=data.split("\n")
data.pop()
answer=0
auxData=[]
for field in data:
    row=field.split("\t")
    for i in range(row.__len__()):
        row[i]=int(row[i])
    auxData.append(row)
for row in auxData:
    for el in row:
        for j in range(row.__len__()):
            if el%row[j]==0 and el!=row[j]:
                answer+=int(el/row[j])
print(answer)