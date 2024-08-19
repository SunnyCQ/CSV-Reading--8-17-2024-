#Converts TSV file to CSV
import csv

input_tsv_file = 'data/ChineseToEnglishSentences.tsv'
output_csv_file = 'data/ChineseToEnglishSentences.csv'

# Open the TSV file for reading and the CSV file for writing
with open(input_tsv_file, 'r', encoding='utf-8') as tsv_file:
    tsv_reader = csv.reader(tsv_file, delimiter='\t')

    with open(output_csv_file, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        # Write all rows from the TSV to the CSV
        for row in tsv_reader:
            csv_writer.writerow(row)

