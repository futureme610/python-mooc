

while True:
    program = input("Editor: ")

    if program.lower() == "visual studio code":
        print("an excellent choice!")
        break

    elif program.lower() == "word" or program.lower() == "notepad":
        print("awful")

    else:
        print("not good")