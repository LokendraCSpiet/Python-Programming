# game.py

# Extending module load path
"""
You can use the environment variable PYTHONPATH to 
specify additional directories to look for modules like this:
# PYTHONPATH=/foo python game.py
"""

# import the draw module
import draw

def play_game():
    return "Start Game..."

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()