def no_shouting(func_list :list):
    is_it_upper = []
    
    for item in func_list:
        if not item.isupper():
            is_it_upper.append(item)
    return is_it_upper

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
    
    # Write your solution here