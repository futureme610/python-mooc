phone_book = {}
while True:
    command = int(input("command(1 search, 2 add, 3 quit): "))

    if command == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(number)
        print("ok!")

    if command == 1:
        name_search = input("name: ")
        if name_search in phone_book:
            for number in phone_book[name_search]:
                print(number)
        else:
            print("no number")

    if command == 3:
        print("quitting...")
        break