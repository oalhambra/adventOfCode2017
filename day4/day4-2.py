f = open("input.txt","r")
data=f.read()

def isAnagram(word1, word2):
    dict={'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,'p':53,
          'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101}
    value1=1
    value2=1
    for i in word1:
        value1*=dict[i]
    for j in word2:
        value2*=dict[j]
    return value1==value2

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
        for el in passw:
            if isAnagram(word, el):
                valid=False
    if valid:
        validPass+=1
print(validPass)
