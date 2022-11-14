def is_adjacent(matrix, node1, node2):
    if matrix[node1] == 1 and matrix[node2] == 1:
        return True
    return False

is_adjacent([
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
], 0, 2)
