
layers = int(input())
grid_size = layers * 2 - 1
center = grid_size // 2

for i in range(grid_size):
    row = ""
    for j in range(grid_size):
        row_distance = abs(i-center)
        col_distance = abs(j-center)
        layer = max(row_distance, col_distance)
        letter = chr(65 + layer)
        row += letter
    print(row)