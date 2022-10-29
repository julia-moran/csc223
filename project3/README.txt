Assignment Instructions:

You are to use the file named netflix_titles.csv which is from the Netflix Movies and TV Shows dataset hosted on Kaggle. 
This file will be converted from the CSV file format into JSON.

Your program will complete the following data processing steps:

  1.  Read the data using the Python CSV library.
  2.  Retrieve the subset of content that have “TV Show” in the type field.
  3.  From this subset, keep the following fields: “show_id”, “title”, “director”, “country”, “date_added”, “duration”.
  4.  Sort the shows in descending order based on the number of seasons (Duration field).
  5.  Write the data to a JSON file using the Python JSON library.

The output must have the following format for each show:

{
    "show_id": id,
    "title": title,
    "director": director,
    "country": country,
    "date_added": date_added,
    "duration": duration
}

The values for each key should be replaced with the respective data. Each show should be it’s own JSON object in the output file. 
Your JSON file should be formatted properly, meaning that all the data is on separate lines as seen in the example output below.

You may hard-code the filename in your program. Meaning, the program is only intended to work with the supplied dataset. 
Your json file can be named anything, but must have a .json file extension.
