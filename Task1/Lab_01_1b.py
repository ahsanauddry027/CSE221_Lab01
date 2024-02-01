readFile = open('input1b.txt','r')
readFile2 = open('output1b.txt','w')

length = readFile.readline()

for nums in range(int(length)):
    newarr = readFile.readline(10)
    ext = readFile.readline().split(" ")
    result=0
    extnum = ext[2].split("\n")[0]
    if ext[1]=="+":
        result = int(ext[0])+int(extnum)
    elif ext[1]=="-":
        result = int(ext[0])-int(extnum)
    elif ext[1]=="/":
        result = int(ext[0])/int(extnum)
    elif ext[1]=="*":
        result = int(ext[0])*int(extnum) 
    
    stri=f"The result of {ext[0]} {ext[1]} {extnum} is {result}\n"
    readFile2.write(stri)