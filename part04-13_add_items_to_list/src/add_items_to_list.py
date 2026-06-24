def list(total):
    list_start = []
    i = 1

    while i <= total:
        item = int(input(f"Item {i}: "))
        list_start.append(item)
        i +=1
    print(list_start)
total = int(input("How many items: "))
list(total)


