def main():
    names, ranks, divs, ids = init_database()
def init_database():
    names = ["Spock", "James Kirk", "Jean-Luc Picard", "Seven of Nine", "Worf"]
    ranks = ["Commander", "Lieutenant", "Captain", "Cadet", "Ensign"]
    divs = ["Command", "Command", "Sciences", "Operations", "Sciences"]
    ids = [0, 1, 2, 3, 4]

    return names, ranks, divs, ids


    

main()