def merge(arr,start,end,mid):
    size1 = mid-start+1
    size2 = end-mid
    
    arr1= [None]*size1
    arr2= [None]*size2
    
    for nums in range(size1):
        arr1[nums] = arr[start+nums]
    for nums in range(size2):
        arr2[nums] = arr[mid+nums+1]    
    
    print(arr1,arr2,"Inside")
    i,j,k=0,0,start
    while i<size1 and j<size2:
        
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
            k+=1
        else:
            arr[k]=arr2[j]
            j+=1
            k+=1
    while i<size1:
        arr[k] = arr1[i]
        i+=1
        k+=1
    while j<size1:
        arr[k] = arr2[j]
        j+=1
        k+=1
    


def mergeDivison(arr,start,end):
    
    if start <end:
        mid = (start+end)//2
        mergeDivison(arr,start,mid)
        mergeDivison(arr,mid+1,end)
        
        print(arr,start,end,mid,"start end mid")
        merge(arr,start,end,mid)
        
        
    
list1 = [6,3,2,1]
mergeDivison(list1,0,len(list1)-1)
print(list1)