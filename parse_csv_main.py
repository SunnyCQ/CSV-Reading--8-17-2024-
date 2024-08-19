import csv
import pickle
from googletrans import Translator #pip install pip install googletrans==4.0.0-rc1
from pypinyin import pinyin #pip install pypinyin

translator = Translator() #translation object

def printCSV(CSVName): #returns none, prints csv
    with open(CSVName, 'r', encoding = 'utf-8') as csv_new_file:
        csv_reader = csv.DictReader(csv_new_file)
        for line in csv_reader:
            print(line)

def find_example_sentence(word, sentences):
    for sentence in sentences.values():
        if word in sentence[0]:
            return sentence
    return None

#readCSVName is the csv containing the chinese words to be translated
#writeCSVName is the new csv file you want to create
#sentencesPickle is the filepath to the pickle file containing example sentences
#columnKey is the name of the column in your readCSVName containing all the words
def transChineseCSV(readCSVName, writeCSVName, sentencesPickle, columnKey): #return writeCSV file name
    with open(readCSVName, 'r', encoding = 'utf-8') as csv_read_file:
        csv_reader = csv.DictReader(csv_read_file)

        with open(sentencesPickle, 'rb') as pickleFile:
            sentences = pickle.load(pickleFile) #loads the sentences I generated
            with open(writeCSVName, 'w', newline='', encoding = 'utf-8') as csv_write_file:
                fieldnames = ['Word', 'Pinyin', 'Translation', 'Example', 'Example_Translation'] #must specify the field names
                csv_writer = csv.DictWriter(csv_write_file, fieldnames = fieldnames)
                csv_writer.writeheader() #will write out the field names as the first line

                for line in csv_reader:
                    sample_sentence = find_example_sentence(line[columnKey], sentences)
                    if(sample_sentence is None):
                        csv_writer.writerow({
                            'Word': line[columnKey],
                            'Pinyin': ' '.join(word[0] for word in pinyin(line[columnKey])),
                            'Translation': translator.translate(line[columnKey], src='zh-cn', dest = 'en').text.capitalize(),
                            'Example': 'N/A',
                            'Example_Translation': 'N/A'
                        })
                    else:
                        csv_writer.writerow({
                            'Word': line[columnKey],
                            'Pinyin': ' '.join(word[0] for word in pinyin(line[columnKey])),
                            'Translation': translator.translate(line[columnKey], src='zh-cn', dest = 'en').text.capitalize(),
                            'Example': sample_sentence[0],
                            'Example_Translation': sample_sentence[1]
                        })
    return writeCSVName

# printCSV(transChineseCSV('data/testChineseCSV.csv', 'data/newChineseCSV.csv', 'data/sentences.pkl', 'Word'))
printCSV(transChineseCSV('data/ChineseAnkiWords.csv', 'data/newChineseAnki.csv', 'data/sentences.pkl', '词语'))




