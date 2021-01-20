#! python3
import time
x = 0
y = 0
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
start_time = time.perf_counter()
for y in range(len(grid[y])):
    print('')
    for x in range(len(grid)):
        print(grid[x][y], end = ' ')
print ("     {:g} s".format(time.perf_counter() - start_time))

i = input()
