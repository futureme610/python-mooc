def even_numbers(my_list):
    even_list = []
    for e in my_list:
        if e % 2 == 0:
            even_list.append(e)
    return even_list
            

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
