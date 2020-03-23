import PyPDF2 
import textract
import re
import nltk 
import os
from os import listdir
from os.path import isfile, join
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


#Define your pdf extension file here
filename = 'demo.pdf'

#Open the file in read mode.
pdfFileObj = open(filename,'rb')

#The readable object pdfReader
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Discerning the pages
num_pages = pdfReader.numPages
count = 0
text = ""

#Loop to canvasing each page of a given file
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
   text = text

else:
   text = textract.process(fileURL, method='tesseract', language='eng')

#Tokanization
tokens = word_tokenize(text)

#Lits of punctuations that we need to clear
punctuations = ['(',')',';',':','[',']',',', '-','/']
stop_words = stopwords.words('english')

#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]

#token = nltk.word_tokenize(keywords)

#I have taken user input to be checked with pdf tokens
query = raw_input("Enter your query:")
qtoken = nltk.word_tokenize(query)
qtags = nltk.pos_tag(qtoken)


qnounsingular = [qtoken for qtoken,tag in qtags
         if re.match("NN*",tag)!=None]


token = nltk.word_tokenize(text)
tags = nltk.pos_tag(token)

nounsingular = [token for token,tag in tags
         if re.match("NN*",tag)!=None]


#Here onwards one can use the matched noun componets for individuals use.
