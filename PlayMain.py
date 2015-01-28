__author__ = 'Andre'

from blackjack import Blackjack
game = Blackjack()
"""game2 = Blackjack()
"""
def main():
    start = input("Would you like to play a round of blackjack?[y/n] ")
    if start == "y":
        game.play()
    reround = input("Would you like to play another round of blackjack?[y/n] ")
    if reround == "y":
        game2 = Blackjack()
        game2.play()

main()