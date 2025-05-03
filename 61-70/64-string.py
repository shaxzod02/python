
def check_paran(text):
    balance = 0


    for index , char in enumerate(text):
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1

        if balance < 0:
            return index
    if balance == 0:
        return 0
    else:
        return -1


text = input("Textni kirting")
print(check_paran(text))