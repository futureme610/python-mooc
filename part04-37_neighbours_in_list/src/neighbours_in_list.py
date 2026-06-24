def longest_series_of_neighbours(num_list):
    num_neigh = 1
    longest = 1

    for i in range(len(num_list) - 1):
        if abs(num_list[i+1] - num_list[i]) == 1:
            num_neigh += 1
            if num_neigh >  longest:
                longest = num_neigh
        else:
            num_neigh = 1
    
    return longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
