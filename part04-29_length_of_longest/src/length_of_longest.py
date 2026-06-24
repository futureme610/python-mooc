def length_of_longest(my_list):
    longest = my_list[0]
    for length in my_list:
        if len(length) > len(longest):
            longest = length
    return len(longest)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
