path =  r'./input.in'
input_file = open(path, 'r')
input_list = input_file.read().splitlines()
sum = 0
sum2 = 0

score_dict = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
score_dict_2 = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}


for entry in input_list:
    sum = sum + score_dict[entry]
    sum2 = sum2 + score_dict_2[entry]

print(sum, sum2)