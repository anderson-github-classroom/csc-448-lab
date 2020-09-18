#!/usr/bin/env python
import sys
import os

student_repo_path="../csc-448-student/"
if os.path.isdir(student_repo_path):
    print("Updating %s"%student_repo_path)
    cmd = "cd %s && git pull"%student_repo_path
    r = os.system(cmd)
    if r != 0:
        print("Command failed:",cmd)
        exit(1)
else:
    cmd = "cd .. && git clone https://github.com/anderson-github-classroom/csc-448-student.git"
    r = os.system(cmd)
    if r != 0:
        print("Command failed:",cmd)
        exit(1)

path = os.getcwd()

# correction in case this is another repo
last = path.split("-")[-1]
try:
    int(last)
    path = path[:(-len(last)-1)]
except:
    pass

identifier = "-".join(path.split("/")[-1].split("-")[:-1])
print("Identifier:",identifier)
name = "".join([c[0].upper()+c[1:] for c in identifier.split("-")])
print("Name:",name)

subdir = None
if "lab-" in identifier:
    print("Auto-detected that this is a lab")
    subdir="labs"
else:
    print("Auto-detected that this is an assignment")
    subdir="assignments"

if subdir is not None:
    if os.path.isfile("%s.ipynb"%name):
        print("File already exists. Rename it and run this program again if you want a fresh copy.")
        exit(1)

    print("Copying %s.ipynb"%name)
    cmd = "cp %s%s/%s.ipynb ."%(student_repo_path,subdir,name)
    r = os.system(cmd)
    if r != 0:
        print("Command failed:",cmd)
        exit(1)

    print('You now have your assignment/lab')
     
