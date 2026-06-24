def double_items(numbers: list):
    doubled_numbers = []
    for i in range(len(numbers)):
        doubled_numbers.append(numbers[i] * 2)
    return doubled_numbers

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
