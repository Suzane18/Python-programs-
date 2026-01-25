def remove_k_digits(num,k):
    st=[]
    for i in num:
        while len(st)and k>0 and st[-1]>i:
            st.pop()
            k-=1
        st.append(i)
    while k>0:
        st.pop()
        k-=1
    result=''.join(st).lstrip('0')
    return result if result else '0'
# Example usage:
print(remove_k_digits("1432219", 3))  # Output: "121"