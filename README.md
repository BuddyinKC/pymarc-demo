# pymarc-demo
Demo script using pyMARC to write MARC records from csv data. This script takes a CSV file in the same folder as the script, iterates through the rows and assigns the data to variables by column name, and then creates MARC records and appends them to a .mrc file in the same folder as the script.

The output MARC file is appended with today's date. Example: output_20251205.mrc.

The script is pretty basic and only includes MARC 100, 245, 260 and 856 fields but it is easy enough to add additional fields to accommodate additional data from the CSV file. 
