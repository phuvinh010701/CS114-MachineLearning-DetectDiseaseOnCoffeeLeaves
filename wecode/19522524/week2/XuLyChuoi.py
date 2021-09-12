st = input()
st = st.lower()
na = ["a", "o", "u", "y", "e", "i"]

st = list(st)

i = 0
len_st = len(st)

while i < len_st:
    if st[i] in na:
        st.pop(i)
        len_st -= 1
    else:
        st.insert(i, ".")
        i += 2
        len_st += 1
    
    

st = "".join(st)
print(st)
