
def find_shortest_word(text):
    words = text.split()
    shortest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

    return f"{shortest_word} {len(shortest_word)}"

text = input("Textni kiriting: ")
print(find_shortest_word(text))