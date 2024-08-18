import csv

with open('englishCSV.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#dictionary writer
    with open('new_csv.csv', 'w', newline = '') as new_file: #newline = '' is to prevent double line printing due to \n and \r\n issues between windows and unix
        fieldnames = ['Greetings'] #must specify the field names
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)

        csv_writer.writeheader() #will write out the field names as the first line

        for line in csv_reader:
            del line['Fruits'] #delete email line when writing, so new csv will not contain it
            csv_writer.writerow(line)