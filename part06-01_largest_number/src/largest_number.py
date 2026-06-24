def largest():
    with open("numbers.txt") as new_file:
        count = 0
        for number in new_file:
            number = int(number.replace("\n", ""))
            if number > count:
                count = number
    return count

if __name__ == "__main__":
    largest()