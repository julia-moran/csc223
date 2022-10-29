# ##########################################################################
#   Author:         Julia Moran                                            #
#   Major:          Computer Science                                       #
#   Creation Date:  February 12, 2022                                      #
#   Due Date:       February 18, 2022                                      #
#   Course:         CSC223 010                                             #
#   Professor Name: Prof. Earl                                             #
#   Assignment:     #2                                                     #
#   Filename:       main.py                                                #
#   Purpose:        This program will accept the name of the file containg #
#                   sales data, read the data, compute the average sales   #
#                   amount, compare the data, and write out the data to a  #
#                   file.                                                  #
# ########################################################################## 

# Function Name: get_data
# Description:   Opens the file and reads in the standard sales from the 
#                first line and a list of the lists of monthly sales from
#                each department.
# Parameters:    filename - string: the name of the file
# Return Values: standard_sales: list of the standard sales
#                total_sales: list of lists of monthly sales for each
#                department
def get_data(filename):
    #Open the file for reading
    with open(filename) as f:
        #Read the first line of the file as the standard sales list
        standard_sales = f.readline()
        standard_sales = standard_sales.strip().split(' ')
        
        #Declare the total sales list
        total_sales = []
        
        #Read the other lines and append each monthly sales amount to the total sales list
        for monthly_sales_amount in f:
            monthly_sales_amount = monthly_sales_amount.strip().split(' ')
            total_sales.append(monthly_sales_amount)

        #Return the standard sales and total sales lists
        return standard_sales, total_sales
        
# Function Name: process_data
# Description:   Using the standard sales and total sales, count the
#                department number and caluclate the average, number of
#                sales less than and greater than the standard sales,
#                and the department's performance to place into a list 
#                of dictionaries containing all of the sales data.
# Parameters:    standard_sales: list of the standard sales
#                total_sales: list of lists of monthly sales for each
#                department
# Return Value:  sales_data: list of the dictionaries containing each
#                department's number, average, number of sales above and
#                below standard, and performance
def process_data(standard_sales, total_sales):
    #Variables
    sales_data = []
    department_number = 0

    
    for j in range(len(total_sales)):
        #Reset the variables for each iteration
        total = 0
        average = 0
        num_sales_above = 0
        num_sales_below = 0
        
        #Increase the department number for each iteration
        department_number += 1

        for i in range(12):
            #Count the total amount of sales for each month
            total = total + float(total_sales[j][i])
            
            #Count the number of sales above and below the standard for each month
            if float(total_sales[j][i]) >= float(standard_sales[i]):
                num_sales_above += 1
            else:
                num_sales_below += 1
        
        #Calculate the average for each department
        average = (total / 12)
        
        #Determine if the performance was satisfactory or not
        if (num_sales_below > 5):
            performace = "unsatisfied"
        else:
            performace = "satisfied"
        
        #Set the calulcated values into a dictionary
        monthly_sales_data = {"Department": department_number, "Average": average, "Above": num_sales_above, "Below": num_sales_below, "Performance": performace}

        #Append each dictionary into a list
        sales_data.append(monthly_sales_data)

    #Return the sales data list of dictionaries
    return sales_data

# Function Name: write_to_file
# Description:   Using the sales data, write the information from that
#                list of dictionaries to a file named out.dat
# Parameters:    sales_data: list of the dictionaries containing each
#                department's number, average, number of sales above and
#                below standard, and performance
# Return Value:  N/A
def write_to_file(sales_data):
    #Open the output file for writing
    f = open("out.dat", 'w')

    #Write a header line to the file
    f.write("Department,Average,Above,Below,Performance\n")

    #Write the values for each department to the output file
    for i in sales_data:
        f.write((str(i["Department"])) + ',')
        f.write((str("{:.1f}".format(i["Average"]))) + ',')
        f.write((str(i["Above"])) + ',')
        f.write((str(i["Below"])) + ',')
        f.write(i["Performance"])

        #Start a new line for each department unless the final department has been reached
        if int(i["Department"]) < (len(sales_data)):
            f.write('\n')
    
    #Close the file
    f.close()    

# Function Name: main
# Description:   Prompts the user for a file name and calls the other
#                functions
# Parameters:    N/A
# Return Values: N/A
def main():   
    #Prompt the user for a filename
    filename = input(("Enter the name of the file: "))
    
    #Call other functions
    standard_sales, total_sales = get_data(filename)
    sales_data = process_data(standard_sales, total_sales)
    write_to_file(sales_data)

#Call the main function
main()
