import re

fname = input('Enter file name ')

try:
    fh = open(fname)
except:
    print('Wrong file name')
    quit()

lst = list()
lst2 = list()


for line in fh:
    lst = line.rstrip()
    #s = str(line)
    y = re.findall('[0-9]+',line)
    if len(y) == 0:
        continue
    #print(y)
    # for x in y:
    #     lst2.append(int(x))
    ls = [lst2.append(int(x)) for x in y]   #using list comprehension by myself over here


print(sum(lst2))