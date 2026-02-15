def main():
    names, ranks, divs, ids = init_database()

    choice = display_menu()

    if choice == 2:
        names, ranks, divs, ids = add_member(names, ranks, divs, ids)

    elif choice == 3:
        names, ranks, divs, ids = remove_member(names, ranks, divs, ids)

    elif choice == 4:
        names, ranks, ids = update_rank(names, ranks,ids)

    elif choice == 1:
        display_roster(names,ranks,divs,ids)

    elif choice == 5:
        search_crew(names, ranks, divs, ids)

    elif choice == 6:
        filter_by_division(names, divs)

    elif choice == 7:
        calculate_payroll(ranks)

    elif choice == 8:
        count_officers(ranks)

    elif choice == 9:
        print("Quiting...")
        


def init_database():
    names = ["Spock", "James Kirk", "Jean-Luc Picard", "Seven of Nine", "Worf"]
    ranks = ["Commander", "Lieutenant", "Captain", "Cadet", "Ensign"]
    divs = ["Command", "Command", "Sciences", "Operations", "Sciences"]
    ids = [0, 1, 2, 3, 4]

    return names, ranks, divs, ids

def display_menu() -> str:
    currentUser = input("User please enter full name:\n")

    while True: 
        try:
            print("Please make a selection" + " " + currentUser)
            print("1) Show database.\n2) Add member.\n3) Remove member.\n4) Update rank.\n5) Search crew.\n6) Filter by division.\n7) Calculate payroll.\n8) Count officers.\n9) Quit.")
            choice = int ( input("Please make a selection:\n"))
            break
        except:
            print("Input invalid\n")

    return choice

def add_member(names, ranks, divs, ids):
    valid_ranks = ["Commander", "Lieutenant", "Captain", "Cadet", "Ensign"]

    while True:
        try:
            addedId = int( input("Please enter ID:\n"))
            if addedId in ids:
                print("ID is already in list.")
            else:
                break
        except:
            print("Please enter integer.")

    while True:
        rank = input("Please enter valid rank:\n")

        if rank not in valid_ranks:
            print("Rank invalid")
        else:
            break

    name = input("Please enter name:\n")
    div = input("Please enter division:\n")
    names.append(name), ranks.append(rank), divs.append(div), ids.append(addedId)
    return names, ranks, divs, ids

def remove_member(names, ranks, divs, ids):
    while True:
        try:
            removalID = int( input("Please enter ID for removal from database:\n"))
            break
        except:
            print("Please enter integer.")

    i = 0
    for id in ids:
        if id == removalID:
            names.pop(i)
            ranks.pop(i)
            divs.pop(i)
            ids.pop(i)
        i += 1
    return names, ranks, divs, ids

def update_rank(names, ranks, ids):
    valid_ranks = ["Commander", "Lieutenant", "Captain", "Cadet", "Ensign"]

    while True:
        try:
            changeID = int( input("Please enter ID to change rank of:\n"))
            break
        except:
            print("Please enter integer.")

    i = 0 
    for id in ids:
        if id == changeID:
            index = i

        i += 1

    print("Changing the rank of: " + names[index])
    while True:
        rank = input("Please enter valid rank to change to:\n")

        if rank not in valid_ranks:
            print("Rank inavlid")
        else:
            ranks[index] = rank
            break

    return names, ranks, ids

def display_roster(names, ranks, divs, ids):
    table = ""

    for i in range( len(names)):
        table += "ID: " + str( ids[i]) + " "
        table += "NAME: " + names[i] + " "
        table += "RANK: " + ranks[i] + " "
        table += "DIVISION: " + divs[i] + "\n"

    print(table)
    return

def search_crew(names, ranks, divs, ids):
    searchTerm = input("Please enter search term:\n")

    for i in range( len(names)):
        if searchTerm in names[i]:
            print ( str( ids[i]) + " " + names[i] + " " + ranks [i] + " " + divs[i] + "\n")
    return


def filter_by_division(names, divs):
    correctDivisions = ["Command", "Sciences", "Operations"]

    while True:
        divisionFilter = input("Please enter division to filter by (Command, Operations, Sciences):\n")
        if divisionFilter not in correctDivisions:
            print("Please enter valid division.")
        else:
            break
    for i in range( len(names)):
            if divs [i] == divisionFilter:
                print(names[i] + " ")
    return

def calculate_payroll(ranks):
    totalPay = 0

    for i in range( len(ranks)):
        if ranks [i] == "Commander":
            totalPay += 1000
        elif ranks [i] == "Lieutenent":
            totalPay += 500
        elif ranks [i] == "Captain":
            totalPay += 200
        elif ranks [i] == "Cadet":
            totalPay += 100
        elif ranks [i] == "Ensign":
            totalPay += 50

    print("Total crew costs: £" + str( totalPay))
    return

def count_officers(ranks):
    totalCount = 0

    for i in range( len(ranks)):
        if ranks[i] == "Commander":
            totalCount += 1
        elif ranks[i] == "Captain":
            totalCount += 1

    print("Amount of officers in databases: " + str(totalCount))
    return
    


main()