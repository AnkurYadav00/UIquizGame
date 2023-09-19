import sys

from question_model import Questions
from quiz_brain import Quiz
from ui import uiInterface


def main():
    # creating class objects for game
    game = Quiz()
    ques = Questions()

    # question and answer bank
    game.generate_question_bank()

    # UI object
    uiInterface(ques, game)


if __name__ == "__main__":
    main()
