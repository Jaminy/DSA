def CountTriplets(arr,N):
    count = 0
    for i in range(N):
        for j in range (i+1,N):
            sum = arr[i] + arr[j]
            #Find whether the sum is there in the array
            for k in range(N):
                if sum == arr[k]:
                    count+=1
    return count

arr=[2, 3, 4]
N=len(arr)
print(CountTriplets(arr,N))
