def valid_parenthesis(s):
    st=[]
    for i in s:
        if i in "({[":
            st.append(i)
        else:
            if not st:
                return False
            top=st.pop()
            if (top=='(' and i!=')') or (top=='{' and i!='}') or (top=='[' and i!=']'):
                return False
    return not st


def valid(s):
    st=[]
    mapping={')':'(', '}':'{', ']':'['}
    for i in s:
        if i in mapping:
            if st:
                top=st.pop()
            else:
                top='#'
            if mapping[i]!=top:
                return False
        else:
            st.append(i)
    return not st
# Example usage:
print(valid("()[]{}"))  # Output: True