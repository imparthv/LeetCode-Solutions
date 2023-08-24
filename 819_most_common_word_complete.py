# 819. Most Common Word
def mostCommonWord(paragraph, banned):
    paragraph = ''.join(filter(lambda x: x.isalpha() or x == ',' or x.isspace(), paragraph.lower()))
    test_list = paragraph.split(',')
    paragraph = " ".join(test_list)
    test_list = paragraph.split()
    word_count = 0
    return_word = ""
    for item in test_list:
        if item not in banned and  test_list.count(item) > word_count:
            word_count = paragraph.count(item)
            return_word = item
    return return_word
    
         
print("Enter the paragraph:")
input_para = input()
banned_list = []
print("Enter banned:")
ban = input()
banned_list.append(ban)
print(mostCommonWord(input_para, banned_list))

