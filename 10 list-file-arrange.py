fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    word=line.split()
    for j in word:
        if j not in lst:
            lst.append(j)
lst.sort()
print(lst)