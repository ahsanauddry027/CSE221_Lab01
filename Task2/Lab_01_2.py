readFile = open('input2.txt','r')
writeFile = open('output2.txt','w')
length = int(readFile.readline().split("\n")[0])
def bubble_sort(arr,n):
    
    for i in range(n):
        flag= False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag ==False:
            break
        
        

# Example usage:
arr = []
list1= readFile.readline().split(" ")
for i in list1:
    arr.append(int(i))
bubble_sort(arr,length)
for n in range(len(arr)):
    # print(n)
    if n==len(arr)-1:
        writeFile.write(str(arr[n]))
    else:
        writeFile.write(str(arr[n])+" ")
        
print("Sorted array:", arr)
