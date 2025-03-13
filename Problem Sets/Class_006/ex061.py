def spiralrotate(matrix):
    matrix.reverse()
    for j, k in enumerate(matrix):
        k.reverse()
    return matrix


def spiral_path(matrix):
    spiral = matrix
    m = len(matrix)
    n = len(matrix[0])
    output = []

    for t in range(min(m, n)):
        output += spiral[0]
        del spiral[0]

        for i, l in enumerate(spiral):
            output.append(l[-1])
            del spiral[i][-1]

        spiralrotate(spiral)

    return output
