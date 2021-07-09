def Kadane(arr): 
      
    max_current = max_global = arr[0]
    N = len(arr)
      
    for i in range(1, N): 
        max_current = max(arr[i], max_current+arr[i])
        max_global = max(max_current, max_global)

    return max_global

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print("Maximum contiguous sum is" , Kadane(arr)) 
            
    
