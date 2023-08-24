# 2586. Count the Number of Vowel Strings in Range
def vowelStrings(words, left, right):
    count = 0
    for i in range(left, right+1):
        if words[i][0] in ['a', 'e', 'i', 'o', 'u'] and words[i][-1] in  ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
   

print(vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4))