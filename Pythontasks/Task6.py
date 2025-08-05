def find_missing(arr,n):
    total_sum = n * (n+1)//2
    newsum = sum(arr) 
    return total_sum - newsum

print("The missing number is : ",find_missing([1,2,4,5],5))
print("The missing number is : ",find_missing([2,3,4,7,1,6,8,9,10],10))