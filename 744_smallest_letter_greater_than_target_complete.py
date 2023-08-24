# 744. Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, target):
    for item in letters:
        if item > target:
            return item
    return letters[0]

print("Enter the string:")
input_string = input()
input_list = [item for item in input_string]
print("Enter the target:")
tar = input()
input_list =sorted(input_list)
out_char = nextGreatestLetter(input_list, tar)
print(out_char)