
def extract_name(text):
    paths = text.split("\\")
    filepath = paths[-1]

    file = filepath.split(".")[0]
    

    return file

text = input("Fileni kiriting: ")
print(extract_name(text))