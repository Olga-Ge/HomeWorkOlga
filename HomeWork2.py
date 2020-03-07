fp= open("harry_potter.txt")
list =[]
fp.contents = fp.read()
punct = "/!£$%&()=?^*+§°ç><,;:.-_{}"
line = ""
for p in fp.contents:
    if p not in punct:
        line =line + p

line = line.split()

for x in line:
    if x not in list:
        list.append(x)

print("Harry Potter has", len(list), "unique words")

fp2 = open ("Moby_Dick")
list2 = []
fp2.contents = fp2.read()
line2 = ""
for p in fp2.contents:
    if p not in punct:
        line2 =line2 + p

line2 = line2.split()

for x in line2:
    if x not in list2:
        list2.append(x)

print("Moby Dick has",len(list2), "unique words")

a=len(list)
b=len(list2)

if a>b:
    print ("Harry Potter rules!")
else:
    print ("Moby Dick author has a wider vocabulary")



