def create_tuple(x: int, y: int, z: int):
    #creates and returns a tuple based on the following criteria:
        # the first element is the smallest of the arguments
        # the second element is the greatest of the arguments
        # the third element is the sum of the arguments

    list = [x, y, z]
    first = min(list)
    second = max(list)
    third = x + y + z
    tuple = (first, second, third)
    return tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))