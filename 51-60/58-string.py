
def remove_exrta_spaces(text):
    text = " ".join(text.split())
    return text

print(remove_exrta_spaces("   Salom   shaxzod"))
print(remove_exrta_spaces(" Asaalom       alaykum"))