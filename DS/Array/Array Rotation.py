def leftRotationByOne(arr,n):
    temp =arr[0]
    for i  in range (n-1):
        arr[i] = arr[i+1]

    arr[n-1] = temp

def leftRotate(arr,n,d):
    for i in range (d):
        leftRotationByOne(arr, n)

arr = [1,2,3,4,5]
d=2
n=len(arr)
leftRotate(arr,len(arr),d)
for i in range (n):
    print(arr[i])
    
