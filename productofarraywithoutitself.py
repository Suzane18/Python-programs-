def product_of_array_without_itself(arr):
    if not arr:
        return []

    n = len(arr)
    output = [1] * n

    # Calculate the prefix products
    prefix_product = 1
    for i in range(n):
        output[i] = prefix_product
        prefix_product *= arr[i]

    # Calculate the suffix products and multiply with the prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= arr[i]

    return output
arr=[1,2,3,4]
print(product_of_array_without_itself(arr))  # Output: [24, 12, 8, 6]