f = open("input.txt","r")
data=f.read()

data=data.split("\n")
data.pop()
processedData=[]
for el in data:
    processedData.append(el.split(" "))

validPass=0
for passw in processedData:
    valid=True
    for i in range(passw.__len__()):
        word=passw.pop()
        if word in passw:
            valid=False
            break
    if valid:
        validPass+=1
print(validPass)