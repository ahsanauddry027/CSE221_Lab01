readFile = open('input3.txt','r')
writeFile = open('output3.txt','w')
noStudents = int(readFile.readline().strip("\n"))
studentId={}

ids = readFile.readline().split(" ")
marks = readFile.readline().split(" ")

for nums in range(noStudents):
    studentId[int(ids[nums])] = int(marks[nums])
    
def sorting(dict_items):
    items = list(dict_items.items())
    for i in range(len(items)): 
        j=i
        while j>0:
            if items[j-1][1]<items[j][1]:
                items[j],items[j-1]=items[j-1],items[j]
            elif items[j-1][1]==items[j][1]:
                if items[j-1][0]>items[j][0]:
                    items[j],items[j-1]=items[j-1],items[j]
            j-=1
             
    return items

sorted = dict(sorting(studentId))
for nums in sorted:
    str=f"ID: {nums} Mark: {sorted[nums]}"
    writeFile.write(str+"\n")
writeFile.close()