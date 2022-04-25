from typing import Dict, List, Union


with open("words.txt") as file:
    data = file.read()
    five_letter_words = data.splitlines()


class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.positions: List[Union[bool, None]] = [None, None, None, None, None]


state = Dict[str, Letter]


def letter_is_eliminated(letter: Letter):
    return all(position == True for position in letter.positions)


def is_word_valid(state: state, possible_word: str) -> bool:
    for (index, letter) in enumerate(possible_word):
        letter_state = state[letter]

        if letter_is_eliminated(letter_state):
            return False

        if letter_state.positions[index] == False:
            return False

        if any(
            other_letter_state.positions[index] == True
            and other_letter_state.letter != letter
            for other_letter_state in state.values()
        ):
            return False
    return True


def get_first_word(state: state) -> Union[str, None]:
    for word in five_letter_words:
        if is_word_valid(state, word):
            return word
    return None


def play_round(current_state):
    word_to_guess = get_first_word(current_state)
    if word_to_guess is None:
        print("No words found")
        return
    result = input(f"Guess the word: {word_to_guess}. What is the result? ").lower()

    if result == "ggggg":
        print("You win!")
        return

    for index, letter in enumerate(word_to_guess):
        if result[index] == "g":
            current_state[letter].positions[index] = True
        elif result[index] == "b":
            current_state[letter].positions = [
                False if position is not True else True
                for position in current_state[letter].positions
            ]
        else:
            current_state[letter].positions[index] = False

    play_round(current_state)


def main():
    current_state = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        current_state[letter] = Letter(letter)
    play_round(current_state)


if __name__ == "__main__":
    main()
