import os
import re 

#BAG OF WORDS COMPONENTS
filecontent = []
hambagofwords = {}
spambagofwords = {}
classify = {}
spamProbability = 0
hamProbability = 0
hamtotalwords = 0
hamdictionarycount = 0
spamtotalwords = 0
spamdictionarycount = 0


#--------------------- RETRIEVE WORDS -------------------------#

def getAllWords(file,filecontent):
     #OPEN THE INPUT FILE
    file = open(file, "r")
    text = file.readlines()

    #GENERATE A LIST OF STRING FROM THE INPUT FILE
    for i in text:
        filecontent.extend(i.split())

    file.close()

     #WRITE RESULTS IN AN OUTPUT FILE
    f = open("output.out", "w")

    #REMOVING THE NON-ALPHANUMERIC CHARACTERS
    for text in filecontent:
        newtext = re.sub('[^a-zA-Z0-9]', '', text.lower())
        filecontent[filecontent.index(text)] = newtext
        
    # #REMOVE THE EMPTY STRINGS ELEMENTS
    while("" in filecontent):
        filecontent.remove("")

    for i in sorted(filecontent):
        f.write(i +"\n")
        
    f.close()


# --------------------- BOG FUNCTION --------------------- #
def bog(filecontent,bagofwords,totalwords,dictionarycount):
    
    #COUNTING THE OCCURENCES OF A WORD
    for text in sorted(filecontent):
        if text in bagofwords.keys():
            bagofwords[text] = bagofwords[text] + 1
        else:
            bagofwords[text] = 1

    #COUNT TOTAL NUMBER OF WORDS
    for i in bagofwords.values():
        totalwords = totalwords + i

    for i in bagofwords.keys():
        dictionarycount = dictionarycount  + 1
        
    # for i in bagofwords.keys():
    #     print(i)   
        
        
    #WRITE RESULTS IN AN OUTPUT FILE
    f = open("output.out", "w")

    f.writelines('Dictionary Size:  ' + repr(dictionarycount) + "\n")
    f.writelines("Total Number of Words: " +repr(totalwords)+"\n")

    for i in bagofwords.keys():
        i = (str(i)).replace('"', '')
        f.write(i + " " + repr(bagofwords[i]).strip('')+"\n")
        
    f.close()


# -------------------- SPAM OR HAM ------------------- #
def classifyIfSpam(word):

    #search for the word in the dictionary
    for word in 






classifyDataPath = "C:/Users/angel/Desktop/cmsc170-exer05-template-main/data/data01/classify"
hamDataPath = "C:/Users/angel/Desktop/cmsc170-exer05-template-main/data/data01/ham"
spamDataPath = "C:/Users/angel/Desktop/cmsc170-exer05-template-main/data/data01/spam"

classifyData = os.listdir(classifyDataPath)
hamData = os.listdir(hamDataPath)
spamData = os.listdir(spamDataPath)

# for file in sorted(hamData):
#     pathA = "C:/Users/angel/Desktop/cmsc170-exer05-template-main/data/data01/ham/"+file
#     getAllWords(pathA,filecontent)

# bog(filecontent,hambagofwords,hamtotalwords,hamdictionarycount)
    
filecontent.clear()

for file in sorted(spamData):
    pathB = "C:/Users/angel/Desktop/cmsc170-exer05-template-main/data/data01/spam/"+file
    getAllWords(pathB,filecontent)

bog(filecontent,spambagofwords,spamtotalwords,spamdictionarycount)

