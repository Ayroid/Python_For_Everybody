# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg=0
ctr=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line.rstrip()
    avg+=float(line[19:])
    ctr+=1
avg=avg/ctr
print("Average spam confidence:",avg)