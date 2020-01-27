# OOP Test

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "Class %%% has-a constructor that takes parameters self, ***",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "Class %%% has-a *** method that takes parameters self, @@@",
    "*** = %%%()":
        "Create an instance of the %%% class and assign it to ***",
    "***.***(@@@)":
        "From ***, get the *** method and call it with parameters self, @@@",
    "***.*** = '***'":
        "From ***, get the *** attribute and set it to '***'"
}

# drill phrases first?
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load the words from URL
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
            random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter names
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# continue until user quits
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            response = input(">  ")

            answer = " ".join(answer.split("\n\t"))

            if response == answer:
                print("Correct!!\n\n")
            else:
                print(f"A: {answer}\n\n")
except EOFError:
    print("\nBye")

