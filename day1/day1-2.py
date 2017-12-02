f = open("input.txt","r")
data=f.read()
answer=0
half=int(data.__len__()/2)
for number in range(data.__len__()):
    if data[number]==data[(number+half)%data.__len__()]:
        answer+=int(data[number])
print(answer)