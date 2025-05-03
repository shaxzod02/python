
def extract_first_file_path(text):
    paths = text.split("/")
    if len(paths)> 2:
        res =paths[1]
    else:
        res = "/"

    return res


text = input("Fileni kiriting: ")
print(extract_first_file_path(text))