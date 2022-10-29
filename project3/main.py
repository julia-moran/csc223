"""
    Author:         Julia Moran
    Major:          Computer Science
    Creation Date:  February 25, 2022
    Due Date:       March 4, 2022
    Course:         CSC223 010
    Professor Name: Prof. Earl
    Assignment:     #3
    Filename:       main.py
    Description:    This program will open the netflix_titles.csv file, sort
                    the TV shows by their duration, and convert the CSV file
                    to a JSON file. 
"""
#Modules
import csv
import json

def readCSV():
    """
    Description:   Opens the file and reads in the data into a list of
                   dictionaries containing the show_ids, titles, directors,
                   countries, dates added, and durations of the TV shows in
                   the file. 
    Parameters:    N/A
    Return Value: 
        showsList: list of the dictionaries containing the data of
                   the TV shows in the file 
    """
    #Initialize the list to hold the dictionaries
    showsList = []
    
    #Open the file to read it with the DictReader
    with open("netflix_titles.csv", 'r', encoding ='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:         
            #Only retrieve the TV shows from the dictionaries
            if row["type"] == "TV Show":
                #Create a new dictionary containing only the specified keys and values from the original dictionaries
                shortenedDict = {}
                shortenedDict["show_id"] = row["show_id"]
                shortenedDict["title"] = row["title"]
                shortenedDict["director"] = row["director"]
                shortenedDict["country"] = row["country"]
                shortenedDict["date_added"] = row["date_added"]
                shortenedDict["duration"] = row["duration"]
                
                #Append the new dictionary to the list
                showsList.append(shortenedDict)
                
    return showsList

def sortFile(data):
    """
    Description: Sorts the file in descending order based on the number of
                 seasons for each show
    Parameters: 
        data: list of the dictionaries containing the data of the
              TV shows in the file
    Return Value: 
        sortedShows: the data list sorted by the duration of the 
                     shows in descending order
    """
    #Convert the part of the duration data that contains the season number to an int value that can be sorted
    for index in range(len(data)):
        data[index]["duration"] = data[index]["duration"].strip().split()
        data[index]["duration"][0] = int(data[index]["duration"][0])

    #Sort the shows by duration in descending order
    sortedShows = sorted(data, key = lambda x: x["duration"][0], reverse = True)
    
    return sortedShows

def writeJSON(data):
    """
    Description:  Writes the sorted data to a JSON file
    Parameters: 
        data: list of the dictionaries containing the data of the
              TV shows in the file
    Return Value: N/A
    """
     
    for dictIndex in range(len(data)):
        #Convert the number of seasons to a string and make the duration into a single string
        data[dictIndex]["duration"] = (str(data[dictIndex]["duration"][0]) + " " + (data[dictIndex]["duration"][1]))

    #Write the data into a JSON file
    with open("netflix_shows.json", 'w') as f:
            json.dump(data, f, indent = 4)

def main():
    """
    Description:  Calls the functions that read, sort, and write the CSV file
    Parameters:   N/A
    Return Value: N/A
    """
    #Function Calls
    data = readCSV()
    data = sortFile(data)
    writeJSON(data)

#Call the main funciton
main()
