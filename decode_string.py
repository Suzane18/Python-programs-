def decode_string(s):
    st=[]
    num=0
    string1=""
    for i in s:
        if i.isdigit():
            num=num*10+int(i)
        elif i=='[':
            st.append((num,string1))
            string1=""
            num=0
        elif i==']':
            num1,prev_string=st.pop()
            string1=prev_string+string1*num1
        else:
            string1+=i
    return string1
# example input
print(decode_string("3[a]2[b]c"))