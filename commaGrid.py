spam = ['apples', 'bananas', 'tofu', 'cats']

def listJoiner(list):
    count = 0
    joined = ''
    while count < len(list) - 2:
        joined += list[count] + ', '
        count += 1
    joined += list[-2] + ' and '
    joined += list[-1] + '.'
    return joined

print(listJoiner(spam))


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
 
