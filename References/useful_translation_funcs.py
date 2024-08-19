from googletrans import Translator #pip install pip install googletrans==4.0.0-rc1
from pypinyin import pinyin #pip install pypinyin

#For pinyin
sample_chinese_word = "你好"
nihao_pinyin = pinyin(sample_chinese_word) #converts word into list of lists containing pinyin


pinyin_str = ' '.join(word[0] for word in nihao_pinyin) #converts pinyin into single string
print(pinyin_str)
print(nihao_pinyin) 






#For translation
translator = Translator() #translation object
translation = translator.translate(sample_chinese_word, src='zh-cn', dest = 'en').text.capitalize()
print(translation)