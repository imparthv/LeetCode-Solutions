# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
def isPrefixOfWord(sentence, searchWord):
    '''
    sentence_list = sentence.split()
    for item in sentence_list:
        if searchWord in item and item.startswith(searchWord):
            return sentence_list.index(item)  + 1
    return -1
    '''
    sentenceList = sentence.split()
    searchWordList = [item for item in sentenceList if item.startswith(searchWord) ]
    if searchWordList:
        return (sentenceList.index(searchWordList[0]) + 1)
    return -1
        
print("Enter sentence and the prefix")
input_sentence = input()
input_prefix = input()

print(isPrefixOfWord(input_sentence, input_prefix))