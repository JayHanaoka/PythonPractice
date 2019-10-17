"""

Given a paragraph and a list of banned words, return the most frequent word that is not in the list
 of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  
Words in the paragraph are not case sensitive.  The answer is in lowercase.

"""

inputString = input().split(' ')
banned = input().split(' ')

def commonWords(inputString, banned):
    words = {}
    
    for word in inputString:
        if word not in banned:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    print(words)
    getMax(words)

def getMax(words):
    result = ["", 0]
    for w in words:
        if words[w] > result[1]:
            result[0] = w
            result[1] = words[w]
    print(result)
    
commonWords(inputString, banned)