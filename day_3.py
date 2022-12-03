from read_input import *

input_list = read_input('input_3.in')

def letter_priority(letter: chr) -> int:
   return ord(letter) % ord('A') + 27 if letter.isupper() else ord(letter) % ord('a') + 1

sum = 0

for entry in input_list:
    common_letter = ''
    left = entry[:len(entry)//2]
    right = entry[len(entry)//2:]
    for letter in left:
        if letter in right:
            common_letter = letter
            break
    sum += letter_priority(common_letter)


sum2 = 0

for i in range(0,len(input_list),3):
    common_letter = ''
    for letter in input_list[i]:
        if letter in input_list[i+1] and letter in input_list[i+2]:
            common_letter = letter
            break 
    sum2 += letter_priority(common_letter)


print(sum, sum2)


