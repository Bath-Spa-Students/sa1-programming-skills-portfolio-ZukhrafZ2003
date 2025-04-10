def search_name(name_list, search_term):
    if search_term in name_list:
        print(f"'{search_term}' was found in the list.")
    else:
        print(f"'{search_term}' was NOT found in the list.")

def main():
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

    # Optional: Take search input from the user
    search_term = input("Enter the name you want to search for: ")

    search_name(names, search_term)

if __name__ == "__main__":
    main()