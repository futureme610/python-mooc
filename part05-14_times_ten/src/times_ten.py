def times_ten(start_index: int, end_index: int):
    #creates and returns a new dictionary
    #keys of the dictionary should be the numbers betweern start and end inclusive
    my_dictionary = {}
    for index in range(start_index, end_index + 1):
        my_dictionary[index] = index * 10
    return my_dictionary

if __name__ == "__main__":    
    d = times_ten(3, 6)
    print(d)
# Write your solution here