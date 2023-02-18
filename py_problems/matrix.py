# A matrix of natural numbers A of size n × m is given.
# It is possible to move from a current cell A(i,j) to any of the 3 adjacent cells in the row i+1, which are A(i+1,j-1), A(i+1,j) and A(i+1,j+1),
# with a penalty A(i,j) is imposed for each pass through the cell (i, j).
# You need to move from some cell at the top of the row to any cell at the bottom of the row,
# by accumulating the minimum penalty for passing through the cells.

def minPathSum(my_list):
    for k in range(m):
        my_list[0][k] = [my_list[0][k]]

    min_value = None
    min_path = None
    for i in range(1, n):
        for j in range(0, m):
            current_tuple = [0, []]
            if j == 0:
                if my_list[i - 1][j][0] <= my_list[i - 1][j + 1][0]:
                    current_tuple[0] = my_list[i - 1][j][0] + my_list[i][j]
                    current_tuple[1] = [i - 1, j]
                else:
                    current_tuple[0] = my_list[i - 1][j + 1][0] + my_list[i][j]
                    current_tuple[1] = [i - 1, j + 1]
            elif j == m - 1:
                if my_list[i - 1][j][0] <= my_list[i - 1][j - 1][0]:
                    current_tuple[0] = my_list[i - 1][j][0] + my_list[i][j]
                    current_tuple[1] = [i - 1, j]
                else:
                    current_tuple[0] = my_list[i - 1][j - 1][0] + my_list[i][j]
                    current_tuple[1] = [i - 1, j - 1]
            else:
                min_elem = min(my_list[i - 1][j][0], my_list[i - 1][j - 1][0], my_list[i - 1][j + 1][0])
                if min_elem == my_list[i - 1][j][0]:
                    current_tuple[0] = my_list[i - 1][j][0] + my_list[i][j]
                    current_tuple[1] = [i - 1, j]
                elif min_elem == my_list[i - 1][j - 1][0]:
                    current_tuple[0] = my_list[i - 1][j - 1][0] + my_list[i][j]
                    current_tuple[1] = [i - 1, j - 1]
                else:
                    current_tuple[0] = my_list[i - 1][j + 1][0] + my_list[i][j]
                    current_tuple[1] = [i - 1, j + 1]
            my_list[i][j] = current_tuple

            if i == n - 1:
                if min_value is None:
                    min_value = current_tuple[0]
                    min_path = [i, j]
                else:
                    if my_list[i][j][0] < min_value:
                        min_value = my_list[i][j][0]
                        min_path = [i, j]

    path = min_path
    cnt = 0
    while path[0] != 0:
        if cnt == 0:
            previous = f"({path[0] + 1},{path[1] + 1}) "
        answer = f"({my_list[path[0]][path[1]][1][0] + 1},{my_list[path[0]][path[1]][1][1] + 1}) " + previous
        previous = answer
        path = my_list[path[0]][path[1]][1]
        cnt += 1
    print(min_value)
    print(previous)


input_list = []

counter = 0
with open('input.txt', 'r') as f:
    for line in f:
        if counter == 0:
            words = line.rstrip('\n')
            n, m = line.split()
            n = int(n)
            m = int(m)
            counter += 1
        else:
            cur_line = line.rstrip('\n')
            cur_list = list(map(int, cur_line.split()))
            input_list.append(cur_list)
            counter += 1

minPathSum(input_list)
