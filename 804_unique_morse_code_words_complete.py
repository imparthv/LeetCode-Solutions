#Unique Morse Code Words
def uniqueMorseRepresentations(words):
    morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....",
                "..",".---","-.-",".-..","--","-.","---",".--.",
                "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_dict = {}
    final_list = []
    char_value = 97
    for item in morse_list:
        morse_dict.update({chr(char_value): item})
        char_value +=1
    for word in words:
        morse_code = ""
        for letter in word:
            morse_code = morse_code + morse_dict.get(letter)
        final_list.append(morse_code)
    return len(set(final_list))

input_list = ["gin","zen","gig","msg"]
output_num = uniqueMorseRepresentations(input_list)
print(output_num)