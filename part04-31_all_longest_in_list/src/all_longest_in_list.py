def all_the_longest(my_list):
    
    new_list = []
    max_length = 0
    
    for word in my_list:
        if len(word) > max_length:
            max_length = len(word)
            
    
    for word in my_list:
        if len(word) == max_length:
            new_list.append(word)
    
    return new_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
        