# Here we need 2 variables to maintain our positions.
# currMin,currItem

# First element current minimum dhore tempItem a store rekhe, pura array iterate krle jdi current minimum theke choto kichu pai oita new current minimum banaia dia tempElement er sthe pura Array iterate howar por swap korte hbe Current item always forward a jaite thakbe (Basically iterate tracker eita.)

def selection(arr):
    
    for i in range(len(arr)):
        currMin = arr[i]
        j = i
        num = 0
        flag= False
        while j<len(arr):
            if currMin>arr[j]: #[3,5,1,-1,4,2,8,7,6]
                currMin = arr[j]
                num = j
                flag = True
            j+=1
        if flag == True:
            arr[i],arr[num]=currMin,arr[i]
    return arr
array = [3,5,1,-1,4,2,8,7,6,0]
sort = selection(array)
print(sort)