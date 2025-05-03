
def check_alpha(text):
    letters = [char for char in text if char.islower()]

    for i in range(1, len(letters)):
        if letters[i] < letters[i-1]:
            return letters[i]

    return 0

text = input("Textni kiriting ")

print(check_alpha(text))