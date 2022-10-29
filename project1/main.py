# ##########################################################################
#   Author:         Julia Moran                                            #
#   Major:          Computer Science                                       #
#   Creation Date:  January 31, 2022                                       #    
#   Due Date:       February 11, 2022                                      #
#   Course:         CSC223 010                                             #
#   Professor Name: Prof. Earl                                             #
#   Assignment:     #1                                                     #
#   Filename:       hw1_payroll.py                                         #
#   Purpose:        This program will accept the names, pay rate, and      #
#                   hours worked for each employee. It will then output    #
#                   the name, gross pay. total withholding amount, and     #
#                   net pay for each employee.                             #
# ##########################################################################


#Input first name
name = input("Enter the employee's name or type done to quit: ")

#While loop for each name
while name != "done":
    
    #Variables
    dayCounter = 1
    totalHoursWorked = 0
    payRate = 0.00
    hoursWorked = 0
    grossPay = 0.00
    withholdingAmount = 0.00
    netPay = 0.00
    stateTax = 0.0
    fica = 0.0
    federalTax = 0.0

    #Get payrate
    payRate = float(input("\nEnter the hourly pay rate: "))

    #Check to make sure the pay rate is not negative
    while payRate <= 0:
        
        print("\nOops! The hourly pay rate must be greater than 0.")
        payRate = float(input("Enter the hourly pay rate: "))

    #Get hours worked for each day
    for i in range(5):
        
        hoursWorked = int(input("\nEnter the hours worked for day " + str(dayCounter) + ": "))
        
        #Check to make sure the hours worked in a day is not negative or greater than 24
        while hoursWorked < 0 or hoursWorked > 24:
            
            print("\nOops! The hours worked in a day must be at least 0 and at most 24.")
            hoursWorked = int(input("Enter the hours worked for day " + str(dayCounter) + ": "))

        totalHoursWorked += hoursWorked
        dayCounter += 1

    #Calculate gross pay
    grossPay = payRate * totalHoursWorked

    #Calculate state tax
    stateTax = grossPay * 0.0307

    #Calculate FICA
    fica = grossPay * 0.0886

    #Calculate federal tax
    if grossPay < 5000:
        federalTax = grossPay * 0.15
    else:
        federalTax = grossPay * 0.25

    #Calculate witholding amount
    withholdingAmount = stateTax + fica + federalTax

    #Calculate net pay
    netPay = grossPay - withholdingAmount

    #Display putput
    print("\nName: " + name)
    print("Gross Pay: ${:.2f}".format(grossPay))
    print("Total witholding amount: ${:.2f}".format(withholdingAmount))
    print("Net pay: ${:.2f}".format(netPay))

    #Get next name
    name = input("\nEnter the employee's name or type done to quit: ")
