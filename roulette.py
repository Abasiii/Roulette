import colors
import number

def play_roulette(balance):
    print(f"{'-'*50}\nWelcome to Roulette! Your current balance is ${balance}\n{'-'*50}")
    print("Do you want to guess a color or a number?")
    guess_type = input("Enter 'color' or 'number': ")
    print(f"{'-'*50}")
    
    if guess_type == "color":
        print("Do you want to guess black or red?")
        guess = input("Enter 'black' or 'red': ")
        payout = 2  # payout for correct color guess is 2x the bet
    elif guess_type == "number":
        print("What number do you want to guess?")
        guess = int(input("Enter a number between 0 and 36: "))
        payout = 36  # payout for correct number guess is 36x the bet
    else:
        print("Invalid input")
        return
    
    print(f"{'-'*50}\nHow much do you want to bet?")
    bet = int(input("Enter an amount: "))
    
    if bet > balance:
        print("Sorry, you don't have enough balance to make that bet")
        return
    
    result = number.generate_number()
    color = colors.RED if result in colors.REDS else colors.BLACK
    print(f"{'-'*50}\nThe result of the spin is {result} - {color}")
    
    if guess_type == "color" and result in colors.BLACK and guess == "black":
        balance += bet * payout
        print(f"Congratulations, you won ${bet * payout}!")
    elif guess_type == "color" and result in colors.REDS and guess == "red":
        balance += bet * payout
        print(f"Congratulations, you won ${bet * payout}!")
    elif guess_type == "number" and result == guess:
        balance += bet * payout
        print(f"Congratulations, you won ${bet * payout}!")
    else:
        balance -= bet
        print("Sorry, better luck next time!")
        
    balance += bet * payout
    
    print(f"{'-'*50}\nYour new balance is ${balance}\n{'-'*50}")
