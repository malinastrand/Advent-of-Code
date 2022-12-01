path =  r'./input.in'
input_file = open(path, 'r')
input_list = input_file.read().splitlines()
sum = 0
sum_list = []
for entry in input_list:
    if entry == '':
        sum_list.append(sum)
        sum = 0
    else:
        sum = sum + int(entry)

sum_list.sort(reverse=True)

print(sum_list[0])

print(sum_list[0]+sum_list[1]+sum_list[2])