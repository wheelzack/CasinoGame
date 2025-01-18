import random

class CasinoGame:
    def __init__(self):
        self.balance = 1000  # Starting balance for the player
        print("Welcome to the Casino! Your starting balance is $1000.")

    def display_rules(self):
        print("\nGame Rules:")
        print("1. You can place bets on numbers (0-36), colors (red/black), or even/odd.")
        print("2. Each round, you decide your bet type and amount.")
        print("3. Winning pays according to the type of bet.")
        print("   - Single number: 35x payout")
        print("   - Color or Even/Odd: 2x payout\n")

    def spin_roulette(self):
        number = random.randint(0, 36)
        color = "red" if number % 2 == 0 else "black"
        return number, color

    def place_bet(self):
        print("\nChoose your bet type:")
        print("1. Number (payout: 35x)")
        print("2. Color (red/black) (payout: 2x)")
        print("3. Even/Odd (payout: 2x)")

        bet_type = int(input("Enter the number corresponding to your choice: "))
        if bet_type == 1:
            bet_value = int(input("Enter the number to bet on (0-36): "))
        elif bet_type == 2:
            bet_value = input("Enter the color to bet on (red/black): ").strip().lower()
        elif bet_type == 3:
            bet_value = input("Enter your choice (even/odd): ").strip().lower()
        else:
            print("Invalid choice! Try again.")
            return self.place_bet()

        bet_amount = int(input("Enter the amount to bet: "))
        if bet_amount > self.balance:
            print("You don't have enough balance! Try again.")
            return self.place_bet()

        return bet_type, bet_value, bet_amount

    def evaluate_bet(self, bet_type, bet_value, bet_amount, number, color):
        print(f"\nThe roulette spun: Number {number}, Color {color}")
        winnings = 0
        if bet_type == 1 and number == bet_value:
            winnings = bet_amount * 35
        elif bet_type == 2 and color == bet_value:
            winnings = bet_amount * 2
        elif bet_type == 3:
            if (bet_value == "even" and number % 2 == 0) or (bet_value == "odd" and number % 2 != 0):
                winnings = bet_amount * 2

        if winnings > 0:
            print(f"Congratulations! You won ${winnings}!")
            self.balance += winnings
        else:
            print("Sorry, you lost this round.")
            self.balance -= bet_amount

    def play(self):
        self.display_rules()
        while self.balance > 0:
            print(f"\nYour current balance: ${self.balance}")
            bet_type, bet_value, bet_amount = self.place_bet()
            number, color = self.spin_roulette()
            self.evaluate_bet(bet_type, bet_value, bet_amount, number, color)

            if self.balance <= 0:
                print("\nYou have no more balance left. Game over!")
                break

            continue_playing = input("Do you want to play another round? (yes/no): ").strip().lower()
            if continue_playing != "yes":
                print(f"\nYou cashed out with a balance of ${self.balance}. Thanks for playing!")
                break

if __name__ == "__main__":
    game = CasinoGame()
    game.play()
