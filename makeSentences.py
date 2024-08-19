#Converts CSV file into a pickle file that can be stored for other files' usage
import pickle
import csv

# ['\ufeff1', '我們試試看！', '413789', "Let's try it."]
def load_tatoeba_sentences(file_path):
    sentences = {}
    with open(file_path, 'r', encoding='utf-8') as tatoeba_file:
        tatoeba_reader = csv.reader(tatoeba_file)
        line = next(tatoeba_reader)
        for line in tatoeba_reader:
            if len(line) >= 4:  # 'cmn' is the code for Mandarin Chinese
                chinese_sent = line[1]
                sentence_id = line[2]
                english_sent = line[3]
                sentences[sentence_id] = (chinese_sent,english_sent)
    return sentences


sentences = load_tatoeba_sentences('data/ChineseToEnglishSentences.csv')

#stores the sentences as a pickle file
with open('data/sentences.pkl', 'wb') as f:
    pickle.dump(sentences, f)

