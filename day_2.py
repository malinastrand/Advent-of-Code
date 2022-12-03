from read_input import *
from enum import Enum

input_list = read_input('input_2.in')

sum = 0
sum2 = 0

move_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}


for entry in input_list:
    opponent = move_dict[entry[0]]
    me = move_dict[entry[2]]
    sum += me

    if opponent == me:
        sum += 3
    if (opponent - me) % 3 == 2:
        sum += 6

    match me:
        case 1:
            sum2 += (opponent - 1 if opponent > 1 else 3)
        case 2:
            sum2 += 3 + opponent
        case 3: 
            sum2 += 6 + (opponent + 1 if opponent < 3 else 1)
        case _:
            print("uh oh!")
 

print(sum, sum2)
