# Taxi Data Analysis with Hadoop
## CS 755 Spring 2018 Assignment 2
## Overview
This folder contains the source code for assignment 2 tasks 1, 2, and 3, as well as a PDF report containing the execution screenshots form EMR and the results of the computations.

Task 2_2 is the sort function for task 2; it takes the output of task 2 as an input.  We output the prior task to s3 and read it into the next step in EMR.

Task 3_2 is the sort function for task 3; it takes the output of task 3 as an input.  We output the prior task to s3 and read it into the next step in EMR.

There is a script, build.sh, included in the root directory.  Executed in any of the 'task' folders this script will compile and package the project.  

View the original source on github: 