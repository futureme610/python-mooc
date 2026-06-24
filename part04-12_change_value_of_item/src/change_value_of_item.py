new_list = [1,2,3,4,5]

index = 0

while True:
    index = int(input("Index: "))
    if index >= 0 and index < len(new_list):
        value = int(input("New value: "))
        new_list[index] = value
        print(new_list)
    else:
        break