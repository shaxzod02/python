
def extract_extension(text):
    return text.split(".")[-1]

text = input("Fileni kiriting: ")
print(extract_extension(text))