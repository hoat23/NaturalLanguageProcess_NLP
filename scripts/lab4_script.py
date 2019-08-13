import nltk                                                                                                      
from nltk.corpus import brown                                                                                    

files = brown.fileids()                                                                                          

with open('somefile.txt', 'a') as dataset:                                                                       
    for file in files:                                                                                           
        texts = []                                                                                               
        for sentence in brown.sents(file):                                                                       
            text = " ".join(str(word) for word in sentence)                                                      
            texts.append(text)                                                                                   
        text_file = " ".join(text for text in texts)                                                             
        dataset.write(text_file + "\n")                                                                          
        print(text_file)    