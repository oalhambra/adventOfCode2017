f = open("input.txt","r")
data=f.read()
data=data.split("\n")
data.pop()
answer=0
for field in data:
    row=field.split("\t")
    for i in range(row.__len__()):
        row[i]=int(row[i])
    answer+=max(row)
    answer-=min(row)
print(answer)


