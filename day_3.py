path =  r'./input.in'
input_file = open(path, 'r')
input_list = input_file.read().splitlines()

sum = 0

for entry in input_list:
    common_type = ''
    left = entry[:len(entry)//2]
    right = entry[len(entry)//2:]
    for letter in left:
        if letter in right:
            common_type = letter
            break

    sum = sum + (ord(letter) % 65 + 27 if letter.isupper() else ord(letter) % 97 + 1)


sum2 = 0

for i in range(0,len(input_list),3):
    print(i)
    common_type = ''
    for letter in input_list[i]:
        if letter in input_list[i+1] and letter in input_list[i+2]:
            common_type = letter
            break 
    sum2 = sum2 + (ord(letter) % 65 + 27 if letter.isupper() else ord(letter) % 97 + 1)


print(sum, sum2)


