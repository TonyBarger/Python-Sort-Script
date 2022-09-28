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
x = input("1 for normal, 2 for Reverse Sort. Enter:")
if x == 1:
        print("Normal Sorting..")
        arr.sort()
        arr.sort(key=len)

elif x == 2:
        print("Reverse Sorting...")
        arr.sort(reverse=True)
        arr.sort(key=len, reverse=True)

f=open('result.txt', 'w')

for i in arr:
    f.write('%s\n' % i)

print("Done")
f.close()

