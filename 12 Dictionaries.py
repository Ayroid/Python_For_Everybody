
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
count=dict()                                        # Dictionary created
handle = open(name)                                 # File Handle
for line in handle:                                 # Iterating through each line of file
    if line.startswith("From:"):                    # Checking if any line starts with From:
        words=line.split()                          # Spliting the line into words
        count[words[1]]=count.get(words[1],0)+1     # Storing the emails which is right after From: so we use index = 1
lk=""
lv=0
for k,v in count.items():                           # Checking for the key with the largest value in the dictionary
    if lv<v or lv is None:
        lv=v
        lk=k

print(lk,lv)