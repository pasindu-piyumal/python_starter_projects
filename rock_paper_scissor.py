import random 
import sys

class RPS:

    def __init__(self):
        print('Welcome to RPS game')

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissor': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input('rock, paper, scissor: ').lower()

        if user_move == 'exit':
            print('Thanks for playing')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()
        
        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move:str, ai_move:str):
        print('_ _ _')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('_ _ _')

    def check_moves(self, user_move:str, ai_move: str):
        if user_move == ai_move:
            print('It\'s a tie')
        elif user_move == 'rock' and ai_move == 'scissor':
            print('You win')
        elif user_move == 'scissor' and ai_move == 'paper':
            print('You win')
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win')
        else:
            print('AI wins')

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()