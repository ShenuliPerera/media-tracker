def show_menu():
    print("Welcome to Media Tracker!")
    print("---------------------------")
    print("1. Add a movie")
    print("2. Add a TV show")
    print("3. Add a Book")
    print("4. View my list")
    print("5. Quit")
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice")

        if choice == "1":
            print ("You choose: Add a movie")
        elif choice == "2":
            print("You choose : Add a   TV show")
        elif choice =="3":
            print("You choose: Add a book")
        elif choice =="4":
            print("You choose: View my list")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice please try again")


main()