f = open("input.txt","r")
data=f.read()

data=data.split("\n")
data.pop()

processedData=[]
for i in data:
    processedData.append(int(i))

position=0
steps=0
while position<processedData.__len__():
    value=processedData[position]
    if value>=3:
        processedData[position]-=1
    else:
        processedData[position]+=1
    position+=value
    steps+=1
print(steps)