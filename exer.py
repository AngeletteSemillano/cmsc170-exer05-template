import os
import re 

#BAG OF WORDS COMPONENTS
filecontent = []
classifywords = []
hambagofwords = {}
spambagofwords = {}
classify = {}
spamProbability = 0
hamProbability = 0
hamtotalwords = 0
hamdictionarycount = 0
spamtotalwords = 0
spamdictionarycount = 0
count = 1


#--------------------- RETRIEVE WORDS -------------------------#

def getAllWords(txtfile,filecontent):
     #OPEN THE INPUT FILE
    # file = open(txtfile, "r")
    with open(txtfile, encoding="utf8", errors='ignore') as file:
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

    return dictionarycount
        
    # for i in bagofwords.keys():
    #     print(i)   
        
        
    # #WRITE RESULTS IN AN OUTPUT FILE
    # f = open("output.out", "w")

    # f.writelines('Dictionary Size:  ' + repr(dictionarycount) + "\n")
    # f.writelines("Total Number of Words: " +repr(totalwords)+"\n")

    # for i in bagofwords.keys():
    #     i = (str(i)).replace('"', '')
    #     f.write(i + " " + repr(bagofwords[i]).strip('')+"\n")
        
    # f.close()


# -------------------- GET SPAM/HAM PROBABILITY ------------------- #
def classifySpamHam(text,bagofwords,dictionarycount):

    #list of the probability of each word found in the spam data
    probabilityList = []

    # stores the spam probability of the file 
    prob = 1    

    #search for the word in the dictionary
    for word in text:
        if word in bagofwords.keys():
            ans = bagofwords[word]/dictionarycount
            probabilityList.append(ans)
    
    for i in probabilityList:
        prob = prob * i

    return prob




classifyDataPath = "/workspaces/cmsc170-exer05-template/data/data01/classify"
hamDataPath = "/workspaces/cmsc170-exer05-template/data/data01/ham"
spamDataPath = "/workspaces/cmsc170-exer05-template/data/data01/spam"

classifyData = os.listdir(classifyDataPath)
hamData = os.listdir(hamDataPath)
spamData = os.listdir(spamDataPath)

for file in sorted(hamData):
    pathA = "/workspaces/cmsc170-exer05-template/data/data01/ham/"+file
    getAllWords(pathA,filecontent)

hamdictionarycount = bog(filecontent,hambagofwords,hamtotalwords,hamdictionarycount)
    
filecontent.clear()

for file in sorted(spamData):
    pathB = "/workspaces/cmsc170-exer05-template/data/data01/spam/"+file
    getAllWords(pathB,filecontent)

spamdictionarycount = bog(filecontent,spambagofwords,spamtotalwords,spamdictionarycount)

filecontent.clear()

f = open("output.out", "w")


for file in sorted(classifyData):
    pathC= "/workspaces/cmsc170-exer05-template/data/data01/classify/"+file
    getAllWords(pathC,filecontent)
    #remove duplicates in the classifydata
    classifywords = sorted(list(dict.fromkeys(filecontent)))
    spamProbability = classifySpamHam(classifywords,spambagofwords,spamdictionarycount)
    hamProbability = classifySpamHam(classifywords,hambagofwords,hamdictionarycount)
    f.writelines(str(count) + " SPAM: " + str(spamProbability) + " HAM: " + str(hamProbability) + "\n")
    
    # update counter
    count = count + 1

    # reset the list that stores the words
    classifywords.clear()
    filecontent.clear()


    


    # if spamProbability > hamProbability:
    #     f.write(count +" SPAM "+ spamProbability+"\n")
    #     count = count + 1

    # elif hamProbability < spamProbability:
    #     f.write(count +" HAM "+ spamProbability+"\n")
    #     count = count + 1


f.close()






     
    #WRITE RESULTS IN AN OUTPUT FILE

        
