from Proj3_repo.App.search import find_similar


query = input("Enter travel preference: ")

results = find_similar(query)


if not results:
    print("\nNo exact match found.")
    print("Here are some popular destinations:\n")

    results = [
        ("Bali", "Indonesia"),
        ("Maldives", "Maldives"),
        ("Paris", "France")
    ]

    for name, country in results:
        print("---------------------")
        print(name)
        print(country)

    exit()


for destination, score in results:

    print("---------------------")
    print(destination.name)
    print(destination.country)
    print(destination.category)
    print("Score:", round(score, 3))