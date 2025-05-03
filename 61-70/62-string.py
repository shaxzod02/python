

def extract_first_file_path(text):
    paths = text.split("/")
    if len(paths)> 3:
        res =paths[-2]
    else:
        res = "/"

    return res


text = input("Fileni kiriting: ")
print(extract_first_file_path(text))