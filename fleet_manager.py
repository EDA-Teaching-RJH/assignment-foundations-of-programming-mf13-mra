def main():
    names, ranks, divs, ids = init_database()

    choice = display_menu()

    if choice == 2:
        names, ranks, divs, ids = add_member(names, ranks, divs, ids)


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
    

main()