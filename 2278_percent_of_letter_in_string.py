# 2278. Percentage of letter in string
def percentageLetter(s, letter):
    letter_count = 0
    if letter in s: letter_count = s.count(letter)
    return int((letter_count/len(s))*100)

print("Enter the input string:")
inputString = input()
print("Enter the letter:")
inputLetter = input()
print(percentageLetter(inputString, inputLetter))