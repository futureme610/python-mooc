phone_book = {}
while True:
    command = int(input("command(1 search, 2 add, 3 quit): "))

    if command == 2:
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")

    if command == 1:
        name_search = input("name: ")
        if name_search in phone_book:
            print(phone_book[name_search])
        else:
            print("no number")

    if command == 3:
        print("quitting...")
        break