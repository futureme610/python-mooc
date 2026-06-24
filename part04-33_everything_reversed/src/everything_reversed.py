def everything_reversed(names: list):
    rev_list = []
    i = len(names) - 1
    while i >= 0:
        rev_list.append(names[i][::-1])
        i -= 1
    return rev_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)

