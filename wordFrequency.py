para = """ I explained nested for loops today 
and lI explained nested for loops today and 
loops are really simple. By the way, loops c  
I explained nested for loops today and loops 
are really simple. By the way, loops c I 
explained nested for loops today and loops are 
really simple. By the way, loops coops are really
 simple. By the way, loops can be 
 used to perform certain comparisons"""

# split the text by spaces and store it in the list

words = para.split()
# print(words)
# count the frequency of each word in the paragraph

#create an empty dictionary
word_dict = {}

#iterate through each word
for word in words:
    #assign count to '0' if the word is already not there in the dictionary
    #else(if it is already found in the dictionary) increment the count
    if word_dict.has_key(word):
        word_dict[word] = word_dict[word] + 1
    else:
        word_dict[word] = 1

# print(word_dict)

for key, value in word_dict.items():
    print("{} : {}".format(key, value))




