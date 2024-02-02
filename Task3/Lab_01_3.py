inputs = [['input3a.txt','output3a.txt'],['input3b.txt','output3b.txt']]

for num in inputs:
    readFile = open(num[0],'r')
    writeFile = open(num[1],'w')

    noStudents = int(readFile.readline().strip("\n"))
    studentId={}

    ids = readFile.readline().split(" ")
    marks = readFile.readline().split(" ")

    for nums in range(noStudents):
        studentId[int(ids[nums])] = int(marks[nums])
        
    def Selectionsorting(dict_items):
        items = list(dict_items.items())
        for i in range(len(items)): 
            currMin = items[i]
            j = i
            num = 0
            flag= False
            while j<len(items):
                if  currMin[1]<items[j][1]:
                    currMin = items[j]
                    num = j
                    flag=True
                elif currMin[1]==items[j][1]:
                    if currMin[0]>items[j][0]:
                        currMin = items[j]
                        num = j
                        flag=True
                j+=1
            if flag==True:
                items[i],items[num] = currMin,items[i] 
        return items
    sort = dict(Selectionsorting(studentId))
    for nums in sort:
        str=f"ID: {nums} Mark: {sort[nums]}"
        writeFile.write(str+"\n")
    readFile.close()
    writeFile.close()
