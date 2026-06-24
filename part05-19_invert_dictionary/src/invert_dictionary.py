def invert(dictionary: dict):
    #dictionary should be inverted in place so that values become keys
    #and keys become values
    invert_dict = {}
    for key, value in dictionary.items():
        invert_dict[value] = key
    dictionary.clear()
    for key, value in invert_dict.items():
        dictionary[key] = value


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)