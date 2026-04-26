import random

def roll_dice(amount: int=2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls,  sum(rolls)

def main():
    while True:
        try:
            user_input: str = input('How many dices would you like to roll? ')
            
            if user_input.lower() == 'exit':
                print('Thanks for playing')
                break
            
            roll, total = roll_dice(int(user_input)) 
            print("Rolls:", end=" ")
            print(*roll, sep=", ")
            print("Total:", total)

        except ValueError:
            print('Please enter a valid number')

if __name__ == '__main__':
    main()