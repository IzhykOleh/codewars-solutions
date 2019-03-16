def reverse_words(text):
    mas = []
    st=""
    txt=""
    print(text)
    for v in text:
        if v==" ": 
            if mas:
                txt = "".join(reversed(mas))
                st=st+txt+" "
                mas = []
            else:
                st+=" "    
        else:
            mas.append(v)
    if mas:
        txt = "".join(reversed(mas))
        st=st+txt
        mas = []
    print(st)
    return st