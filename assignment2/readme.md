# NYC Taxi Data Analysis with Hadoop on AWS EMR
## Assignment 2 CS 755 Spring 2018 
## Group Three
### 2/27/2018

- Dan Budris
- Don Yoo
- Kanchan Mohite
- Corey Drees

## Overview
This folder contains the source code for assignment 2 tasks 1, 2, and 3, as well as a PDF report containing the execution screenshots from EMR and the results of the computations.

Task 2_2 is the sort function for task 2; it takes the output of task 2 as an input.  We output the prior task to s3 and read it into the next step in EMR.

Task 3_2 is the sort function for task 3; it takes the output of task 3 as an input.  We output the prior task to s3 and read it into the next step in EMR.

There is a script, build.sh, included in the root directory.  Executed in any of the 'task' folders this script will compile and package the jar file.