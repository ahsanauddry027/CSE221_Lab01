def descending(arr):
    
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]<arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
            
def ascending(arr):
    
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
            
arr1=[10,12,45,45,34,13]
arr=[10,12,12,45,34,13]


descending(arr1)
ascending(arr)

print(arr1)
print(arr)