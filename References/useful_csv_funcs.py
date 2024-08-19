import csv
#Note: Do not run this, this is for documentation purposes only


#to read a csv:
#this : version allows automatic file closing once loop is exited
with open('TestCSVEng.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

#to write a csv:
#if the csv doesn't exist, it'll simply make one with the name. If it already exists, it overwrites it
with open('new_csv.csv', 'w', newline = '') as new_file: #newline = '' is to prevent double line printing due to \n and \r\n issues between windows and unix
    csv_writer = csv.writer(new_file, delimiter = '-') #delimiter setting is optional, but this is how you do it

#another way to read and write
#these methods are manual, so must manually close it. Also, if error occurs before closing, might not close at all...
#the _file is the actual file, while the _simple is the csv_object

#read:
csv_reader_file = open('TestCSVEng.csv', 'r')
csv_reader_simple = csv.reader(csv_reader_file)

#write:
csv_writer_file = open('new_names.csv', 'w')
csv_writer_simple = csv.writer(csv_writer_file)

#dictionary reader
with open('englishCSV.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
#prints things out as a dictionary, with the first row representing the names of the values
#example: 
# {'Greetings': 'Hello', ' Fruits': ' Apples'}
# {'Greetings': 'Goodbye', ' Fruits': ' Oranges'}
#makes it easier to index specific values

    #will print only the fruits line
    for line in csv_reader:
        print(line['fruits'])
        

#dictionary writer
    with open('new_csv.csv', 'w', newline = '') as new_file: #newline = '' is to prevent double line printing due to \n and \r\n issues between windows and unix
        fieldnames = ['Greetings', 'Fruits'] #must specify the field names
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)

        csv_writer.writeheader() #will write out the field names as the first line

        for line in csv_reader:
            csv_writer.writerow(line)
    
    #OR
    with open('new_csv.csv', 'w', newline = '') as new_file: #newline = '' is to prevent double line printing due to \n and \r\n issues between windows and unix
        fieldnames = ['Greetings'] #Fruits not included this time
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)

        csv_writer.writeheader() #will write out the field names as the first line
        
        for line in csv_reader:
            del line['Fruits'] #delete email line when writing, so new csv will not contain it
            csv_writer.writerow(line)

#to skip a value in a csv:
skipped_value = next(csv_reader_simple)

#to print all the values in csv:
for line in csv_reader_simple:
    print(line)

#to set the position of the file to some specific line
#note how we set the file's position, not the reader's
csv_reader_file.seek(0) #0 is the first line

#to print first value in each line
for line in csv_reader_simple:
    print(line[0])

#to close a file. rememebr, we are closing the file, not the csv object..
csv_reader_file.close()
csv_writer_file.close()



#Values can be specified using indexing. 
#line[0] gives first value of line