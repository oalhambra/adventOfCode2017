f = open("day1.txt","r")
data=f.read()
answer=0

for number in range(data.__len__()-1):
    if data[number]==data[number+1]:
        answer+=int(data[number])
if data[-1]==data[0]:
    answer+=int(data[-1])
print(answer)