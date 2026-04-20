class Game:
    def __init__(self):
        self.is_running = True

    def start(self):
        print("Welcome to the Country Supremacy Game!")
        while self.is_running:
            self.show_menu()

    def show_menu(self):
        print("\nMain Menu:")
        print("1. Start Game")
        print("2. Instructions")
        print("3. Exit")

        choice = input("Enter your choice: ")
        self.handle_choice(choice)

    def handle_choice(self, choice):
        if choice == "1":
            print("Starting the game...")
            self.start_game()
        elif choice == "2":
            self.show_instructions()
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            self.is_running = False
        else:
            print("Invalid choice. Please try again.")

    def start_game(self):
        print("Game logic goes here.")

    def show_instructions(self):
        print("Instructions for playing the game go here.")


if __name__ == "__main__":
    game = Game()
    game.start()