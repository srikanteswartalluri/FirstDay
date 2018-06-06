para = """I explained nested for 
loops today and lI explained nested for 
loops today and loops are really simple. 
By the way, loops c  I 
explained nested for loops 
today and loops are really simple. 
By the way, loops c I explained nested 
for loops today and loops are really simple.
 By the way, loops coops are really simple.
  By the way, loops can be used to perform certain
   comparisons word"""

lines = para.split("\n")
words = []
for line in lines:
    print line
    #words
    lwords = line.split()
    for word in lwords:
        words.append(word)

print(words)
print("wordcount: {}".format(len(words)))

