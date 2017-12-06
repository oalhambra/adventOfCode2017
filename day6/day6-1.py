f = open("input.txt","r")
data=f.read()

data=data.split("\t")
processedData=[]
for i in data:
    processedData.append(int(i))
previousStates=[]
keepGoing=True
cycles=0

while keepGoing:
    cycles+=1
    previousStates.append(str(processedData))
    value=max(processedData)
    position=processedData.index(value)
    processedData[position]=0
    position+=1
    for i in range(value):
        processedData[position%processedData.__len__()]+=1
        position+=1
    if str(processedData) in previousStates:
        keepGoing=False



print(cycles)