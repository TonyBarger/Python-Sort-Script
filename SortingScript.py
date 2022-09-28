import sys, os, glob
os.scandir(os.getcwd())
for file in glob.glob("*.txt"):
        file = file
f = open(file)
arr=[]
for line in f:
    strip_lines=line.strip()
    arri=strip_lines.strip("\n")
    m=arr.append(arri)
f.close()

arr.sort()
arr.sort(key=len)


f=open('result.txt', 'w')

for i in arr:
    f.write('%s\n' % i)

f.close()

