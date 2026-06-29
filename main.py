def show_menu():
    print("Welcome to Media Tracker!")
    print("---------------------------")
    print("1. Add a movie")
    print("2. Add a TV show")
    print("3. Add a Book")
    print("4. View my list")
    print("5. Quit")

movies = []
def add_movie():
    title = input("Enter movie title: ")
    rating = input("Rate it out of 10: ")
    movie = {"title": title, "rating": rating}
    movies.append(movie)
    print(f"'{title}' added to your list!done")


def view_list():
    if len(movies) == 0:
        print("Your list is empty!")
    else:
        print("\nYour movies:")
        print("---------------------------")
        for movie in movies:
            print(f"- {movie['title']} | Rating: {movie['rating']}/10")


def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice")

        if choice == "1":
            print ("You choose: Add a movie")
            add_movie()
        elif choice == "2":
            print("You choose : Add a   TV show")
        elif choice =="3":
            print("You choose: Add a book")
        elif choice =="4":
            print("You choose: View my list")
            view_list()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice please try again")


main()