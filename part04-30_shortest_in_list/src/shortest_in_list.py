def shortest(my_list):
    short_word = my_list[0]
    for word in my_list:
        if len(word) < len(short_word):
            short_word = word
    return short_word


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)