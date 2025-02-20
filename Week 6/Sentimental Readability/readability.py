import sys

from cs50 import get_string

text = get_string("Text: ")
alphas = 0
digits = 0
special_characters = 0
words = 1
sentences = 0

if text:
    for i, item in enumerate(text):
        if item.isalpha():
            alphas += 1
        elif item.isnumeric():
            digits += 1
        elif item == "?" or item == "!" or item == ".":
            sentences += 1
        elif item == " " and text[i + 1]:
            words += 1
        else:
            special_characters += 1

    letters = float(alphas / words * 100)
    sentences = float(sentences / words * 100)

    # Calculate readability
    index = round((float)(0.0588 * letters - 0.296 * sentences - 15.8))

    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade", index)

    sys.exit()
