my_list = []
i = 1
while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "d":
        my_list.append(i)
        i += 1
    
    elif choice == "r":
        my_list.pop()
        i -= 1
    
    elif choice =="x":
        print("Bye!")
        break