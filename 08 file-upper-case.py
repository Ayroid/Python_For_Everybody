fname = input("Enter file name: ")
fh = open(fname)
fr = fh.read()
fr.strip()
print(fr.upper())