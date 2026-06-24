# write your solution here
def matrix_format():
    formatted_matrix = []
    matrix_row = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for number in numbers:
                matrix_row.append(int(number))
            formatted_matrix.append(matrix_row)
            matrix_row = []
    
    return formatted_matrix
        


def matrix_sum():
    formatted_matrix = matrix_format()
    sum = 0
    for line in formatted_matrix:
        for number in line:
            sum += number
    return sum

def matrix_max():
    formatted_matrix = matrix_format()
    max = 0
    for line in formatted_matrix:
        for number in line:
            if number > max:
                max = number
    return max

     # go through the matrix and return the maximum

def row_sums():
    formatted_matrix = matrix_format()
    row_sum = 0
    row_sum_list = []
    for line in formatted_matrix:
        for number in line:
            row_sum += number
        row_sum_list.append(row_sum)
        row_sum = 0
    return row_sum_list
#     # returns a list containing the sum of each row in the matrix

if __name__ == "__main__":
    print(f"sum is {matrix_sum()}")
    print(f"max is {matrix_max()}")
    print(f"row sum is {row_sums()}")