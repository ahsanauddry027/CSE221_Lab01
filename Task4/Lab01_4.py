readFile = open('input4.txt','r')
writeFile = open('output4.txt','w')

intputnum = readFile.readline().split("\n")[0]
sort = {}
for nums in range(int(intputnum)):
    
    info = readFile.readline().split(" ")
    place = info[4]
    time1 = info[6].split("\n")[0].split(":")[0]
    time2 = info[6].split("\n")[0]
    
    names = info[0]
    num=0
    for nums in names:
        num += ord(nums)
    if ord(names[0]) not in sort:
        sort[ord(names[0])] = [[names,num,int(time1),place,time2]]
    else:
        sort[ord(names[0])]+= [[names,num,int(time1),place,time2]]

def ascending(dic):
    newlist = list(dic.items())
    for i in range(len(newlist)):
        j=i
        while j>0 and newlist[j-1][0]>newlist[j][0]:
            newlist[j],newlist[j-1]=newlist[j-1],newlist[j]
            j-=1
    return newlist
    
newsort= dict(ascending(sort))

for nums in newsort:
    key = newsort[nums]

    for i in range(len(key)):
        k=i
        while k>0:
            if key[k-1][1]>key[k][1]:
                key[k],key[k-1]=key[k-1],key[k]
            elif key[k-1][1]==key[k][1]:
                if key[k-1][2]<key[k][2]:
                  key[k],key[k-1]=key[k-1],key[k]
            k-=1
            
for nums in newsort:
    
    for num in newsort[nums]:
        stri = f"{num[0]} will departure for {num[3]} at {num[4]}\n"
        writeFile.write(stri)