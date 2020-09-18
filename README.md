# CSC 448 Template Lab
This is a blank repo containing information about working on and submitting your labs and assignments.

## Get the lab in the recommended way
python ./get_assignment.py # this should work assuming your directory name hasn't been munged

## Get the lab manually
* Issue the following command once (not needed again) on your system:
    * ``git clone https://github.com/anderson-github-classroom/csc-448-student ../csc-448-student``
* Copy the lab/assignment notebook over

## Local autograding
* Issue this command everytime you want to test. It will try to automatically detect what assignment you are working on.
    *  ./run_tests_locally.sh or python run_tests_locally.py
* You can always try to test specific questions using:
    * pytest ../csc-448-student/tests/test_Syllabus.py::test_question_1

## Remove autograding
Use git to add/commit/push. Check under GitHub actions


## Old information that has been deprecated below

* The lab assignments are located in https://github.com/anderson-github-classroom/csc-448-student
* You will only need to clone csc-448-student repo once. Each week (or more frequent) you can issue a ``git pull`` and receive updated information.
* You should not make changes inside csc-448-student. It should be viewed as read only; however, if you do make changes, please copy/save them manually and then issue a ``git stash`` before trying ``git pull``.
* To work on your lab, click on the link in the schedule, accept the GitHub assignment which will create you an individual repo. 
* When you are done with the lab (or whenever you want), add your changes, commit your changes, and push your changes.

### Old Instructions
* Issue the following command once (not needed again) on your system:
    * ``git clone https://github.com/anderson-github-classroom/csc-448-student ../csc-448-student``

* Issue the following command at the beginning (do not use this command again unless you want to overwrite your work)
    * ``
* Issue this command everytime you want to test. It will try to automatically detect what assignment you are working on.
    *  ./run_tests_locally.sh or python run_tests_locally.py
* You can always try to test specific questions using:
    * pytest ../csc-448-student/tests/test_Syllabus.py::test_question_1
