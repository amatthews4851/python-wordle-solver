from main import Letter, get_first_word


def is_black(letter: str, answer: str):
    return letter not in answer


def is_yellow(letter: str, index: int, answer: str):
    return letter in answer and answer[index] != letter


def is_green(letter: str, index: int, answer: str):
    return answer[index] == letter


def grade_letter(letter: str, index: int, answer: str):
    if is_black(letter, answer):
        return 'b'
    if is_yellow(letter, index, answer):
        return 'y'
    if is_green(letter, index, answer):
        return 'g'
    return 'b'


def grade_guess(guess: str, answer: str):
    return "".join([grade_letter(letter, index, answer)
            for index, letter in enumerate(guess)])


def play_round(answer, current_state, iteration=1):
    word_to_guess = get_first_word(current_state)
    if word_to_guess is None:
        print("❌ No words found:", answer)
        return
    result = grade_guess(word_to_guess, answer)

    if result == "ggggg":
        print(f"✅ Correctly guessed {word_to_guess} on {iteration} guesses")
        return

    for index, letter in enumerate(word_to_guess):
        if result[index] == "g":
            current_state[letter].positions[index] = True
        elif result[index] == "b":
            current_state[letter].positions = [
                False if not position else True for position in current_state[letter].positions]
        else:
            current_state[letter].positions[index] = False

    if iteration >= 6:
        print(f"❌ Failed to guess {word_to_guess} after {iteration} guesses")
        return

    play_round(answer, current_state, iteration + 1)


def main():
    with open("answers.txt") as file:
        data = file.read()
        answers = data.splitlines()
    
    for answer in answers:
        current_state = {}
        for letter in "abcdefghijklmnopqrstuvwxyz":
            current_state[letter] = Letter(letter)
        play_round(answer.lower(), current_state)


if __name__ == "__main__":
    main()
