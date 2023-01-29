# filehandling in python
# write
file=open("newfile.txt","w")
file.write("hello bro")
file.write("hii")
file.close()

file=open("newfile.txt","r")
print(file.read())

file=open("newfile.txt","a")
file.write("how are you")
file.write("where are you going")
file.close()

file=open("newfile.txt","r")
print(file.read())

import os.path
file_path=(r"C:\Users\dell\PycharmProjects\programming\newfile.txt")
flag=os.path.isfile(file_path)
if flag:
    print(f"the file {file_path} exists")
else:
    print(f"the file {file_path} doesnot exist")

import os
file_path=(r"C:\Users\dell\PycharmProjects\programming\newfile.txt")
flagg=os.path.getsize(file_path)
print(f"the file size is {flagg}","bytes")

with open(r"C:\Users\dell\PycharmProjects\programming\newfile.txt")as fp:
    for count, line in enumerate(fp):
        pass
    print("the total line is",count+1)

with open(r"C:\Users\dell\PycharmProjects\programming\newfile.txt") as fp:
    line_no=[1,2]
    lines=[]
    for i, lines in enumerate(fp):
        if i in line_no:
            lines.append(line.strip())
        elif i>5:
            break
print(lines)