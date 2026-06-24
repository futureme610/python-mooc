def sum_of_positives(my_list):
    pos_list = []
    for i in my_list:
        if i > 0:
            pos_list.append(i)
    
    return sum(pos_list)

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)