
def  extract_str(text):

    if text.count(" ") == 1:
        return ""
    
    first_space_index = text.find(" ")
    last_space_index = text.rfind(" ")

    if first_space_index != -1 and last_space_index != -1 and first_space_index != last_space_index:
        res = text[first_space_index + 1:last_space_index]
    else:
        res = ""
    return res    


text = input("Textni kiriting: ")
print(extract_str(text))            