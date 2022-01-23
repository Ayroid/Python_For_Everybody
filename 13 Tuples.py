name = input()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    if line.startswith("From:") or line.startswith("From"):
        words=line.split()
        for word in words:
            if ":" in word and "From:" not in word:
                time=word.split(":")
                count[time[0]]=count.get(time[0],0)+1

lst=list()
for k,v in count.items():
    lst.append((k,v))
lst=sorted(lst)

for k,v in lst:
    print(k,v)
