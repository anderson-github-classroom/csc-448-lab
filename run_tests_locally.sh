#!/bin/bash
for file in `ls *.ipynb`; do
  echo "Testing $file"
  pytest ../csc-448-student/tests/test_Syllabus.py
done;

