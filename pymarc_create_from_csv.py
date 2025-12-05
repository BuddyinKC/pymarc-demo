import pymarc, pandas as pd
import os
from datetime import datetime
mypath = os.path.dirname(os.path.abspath(__file__))

#Read CSV file in the same folder as this script.
df = pd.read_csv('mospace.csv')

#Build MARC file name with today's date
today = datetime.now()
date_string = today.strftime("%Y%m%d")
base_filename = "output"
new_filename = f"{base_filename}_{date_string}.mrc"

#Iterate through the csv data and assign values to variables
for index, row in df.iterrows():
    title = row['Title']
    by = row['By']
    author = row['Author']
    date = row['Date']
    format = row['Format']
    access = row['URI']
#Create MARC record using the variables
    new_record = pymarc.Record()
    new_field_245 = pymarc.Field(
        tag = '245',
        indicators = ['0','0'],
        subfields = [
            pymarc.Subfield(code = 'a', value = title + ' /'),
            pymarc.Subfield(code = 'c', value = by)
        ]
    )
    new_field_100 = pymarc.Field(
        tag = '100',
        indicators = ['1', ' '],
        subfields = [
            pymarc.Subfield(code = 'a', value = author)
        ]
    )
    new_field_260 = pymarc.Field(
        tag = '260',
        indicators = [' ', ' '],
        subfields = [
            pymarc.Subfield(code = 'c', value = date)
        ]
    )
    new_field_856 = pymarc.Field(
        tag = '856',
        indicators = ['4', '0'],
        subfields = [
            pymarc.Subfield(code = 'z', value = 'Access record in MOspace'),
            pymarc.Subfield(code = 'u', value = access)
        ]
    )
    new_record.add_ordered_field(new_field_100)
    new_record.add_ordered_field(new_field_245)
    new_record.add_ordered_field(new_field_260)
    new_record.add_ordered_field(new_field_856)
#Append record to output.mrc file
    with open(mypath+'/'+new_filename, 'ab') as f:
        f.write(new_record.as_marc())
        f.write(b'\n')
        f.write(b'\n')
#Print record to terminal and MARC file name
    print(new_record)
    print(f"File '{new_filename}' created.")
