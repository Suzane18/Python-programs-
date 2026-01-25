def gcd_array(arr):
    mn=arr[0]
    mx=arr[0]
    for i in range(len(arr)):
        if arr[i]<mn:
            mn=arr[i]
        if arr[i]>mx:
            mx=arr[i]
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    return gcd(mn,mx)
# example imput
print(gcd_array([12,15,9,27,6]))  # Output: 3