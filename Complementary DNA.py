def DNA_strand(dna):
    s=''
    for i in dna:
        if i=="A":
            i="T"
        elif i=="T":
            i="A"
        elif i=="C":
            i="G"
        elif i=="G":
            i="C"
        s=s+i
    return s
