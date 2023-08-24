# 824. Goat Latin
def toGoatLatin(sentence):
    s_list = sentence.split()
    count = 0
    final_list = []
    for item in s_list:
        i = 0
        if item[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            word = item + 'ma'
            
        else:
            word = item[1: len(item)+1] + item[0] + 'ma'
        while i <= count:
            word = word + 'a'
            i +=1
        final_list.append(word)
        count += 1
    return (" ").join(final_list)

print("Enter the sentence:")
input_sentence = input()
output_sentence = toGoatLatin(input_sentence)
print(output_sentence)