with open('aaa.txt', 'r') as myfile:
    words=myfile.read().split()
    for i in range(0, len(words)):
        numberF = int(words[i].count('F'))#Count the number of F
        numberC = int(words[i].count('C'))#Count the number of C
        numberK = int(words[i].count('K'))#Count the number of K
        numberR = int(words[i].count('R'))#Count the number of R
        numberf = int(words[i].count('f'))#Count the number of f
        numberc = int(words[i].count('c'))#Count the number of c
        numberk = int(words[i].count('k'))#Count the number of k
        numberr = int(words[i].count('r'))#Count the number of r
        total_bad = numberF + numberC + numberK + numberR + numberf + numberc + numberk + numberr
        total_good = len(words[i]) - total_bad
        if total_bad > total_good:
            print(words[i], ": is bad word")
        else:
            print(words[i], ": is a good word")
        
