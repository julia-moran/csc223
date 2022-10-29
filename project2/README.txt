Assignment Instructions:

A department store needs a program to calculate the sales statistics for it’s various departments each year. T
his store has a standard sales amount (in thousands of dollars) for each month based on data from previous years.

The monthly sales amount are stored in a file sales.dat. The first line of the file contains the standard sales amount for each month. 
Each line that follows contains the twelve sales amounts for that department.

Write a program to calculate statistics for each department in the store. Your program should do the following:

  1.  Prompt the user for the input file name.
  2.  Read the file data into a list and a list of lists.
  3.  Compute the average monthly sales for each department.
  4.  Compare each monthly sales amount with the standard.
  5.  Write the statistics for the department, including the department number, average sales amount, number of months above and below the 
      standard, and performance to a file. The program should output “unsatisfied” as the performance of the department if more than five months 
      are below standard and “satisfied” otherwise.

Your output file must be formatted as follows:

Department,Average,Above,Below,Performance

and each subsequent line contains the appropriate values in the correct order separated by commas. 
The average value must be output with one decimal point of precision. 
