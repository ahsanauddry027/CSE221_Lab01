read_obj = open('input1a.txt','r')
write_obj = open('output1a.txt','w')

for nums in range(int(read_obj.readline())):
    number = int(read_obj.readline().split("\n")[0])
    stri = ""
    if number%2==0:
        stri=f"{number} is an Even number.\n"
    else:
        stri=f"{number} is an Odd number.\n"
    write_obj.write(stri)
read_obj.close()
write_obj.close()
    
        