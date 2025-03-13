def alive_cells(numAlive, cur, i, j, grid, r, c):
    if len(cur) == 2:
        if cur != [0, 0]:
            numAlive += dic[grid[i + cur[0]][j + cur[1]]]
    else:
        pos_rm = []
        pos = [-1, 0, 1]
        if not cur:
            if i == 0:
                pos_rm.append(pos[0])
            if i == r-1:
                pos_rm.append(pos[-1])
        else:
            if j == 0:
                pos_rm.append(pos[0])
            if j == c-1:
                pos_rm.append(pos[-1])

        for pos_add in [element for element in pos if element not in pos_rm]:
            numAlive = alive_cells(numAlive, cur + [pos_add], i, j, grid, r, c)

    return numAlive


def is_alive(cell):
    return cell == "#"


r, c, k = [int(num) for num in input().split(" ")]
grid = [list(input()) for i in range(r)]
dic = {".": 0, "#": 1}
grid_copy = [[x for x in row] for row in grid]

for gen in range(k):
    for i in range(r):
        for j in range(c):
            numAlive = alive_cells(0, [], i, j, grid, r, c)

            if is_alive(grid_copy[i][j]):
                if numAlive <= 1 or numAlive >= 4:
                    grid_copy[i][j] = "."
            else:
                if numAlive == 3:
                    grid_copy[i][j] = "#"

    grid = [[x for x in row] for row in grid_copy]

for row in grid:
    print("".join(row))
