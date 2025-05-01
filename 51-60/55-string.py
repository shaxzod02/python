
def count_words(text):
    textList = text.split()
    count = len(textList)
    return count

text = input("Textni kiriting: ")
print(count_words(text))