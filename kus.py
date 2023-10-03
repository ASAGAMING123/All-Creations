st = str(input("Enter a string:"))
dic = {}
for ch in st:
    dic[ch] = st.index(ch)
for key in dic:
    print(key,":",dic[key])