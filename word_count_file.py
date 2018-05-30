from Helper import text_processing

def frequency_finder(text):
    freq = {}
    #write code
    print("details : {}".format(freq))


f = open("news")
text = f.read()
#print word count
text_processing.word_count(text)
#print frequency of each word
frequency_finder(text)
f.close()