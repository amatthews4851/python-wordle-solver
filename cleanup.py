with open("raw_words.txt") as file:
    data = file.read()
    words = data.splitlines()
    five_letter_words = [word.lower() for word in words if len(word) == 5 and word.isalpha() and word.isascii()]
    unique_five_letter_words = list(dict.fromkeys(five_letter_words))
    with open("words.txt", "w") as new_file:
      new_file.write("\n".join(unique_five_letter_words))
