def oldest_person(people: list):
    #first element in tuple is the name
    #second elemen in tuple is the year of birth
    #function should find the oldest person and return their name

    oldest_person = ["", 0]
    for person in people:
        
        if oldest_person[1] == 0:
            oldest_person = person
        
        if person[1] < oldest_person[1]:
            oldest_person = person

    return oldest_person[0]
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))