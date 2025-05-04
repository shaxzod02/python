
def atm():
    # Initialize variables
    parol1 = 1111
    mablag = 10000000

    # Language selection
    print("1. UZB")
    print("2. RUS")
    print("3. ENG")
    til = int(input("Choose a language / Выберите язык / Tilni tanlang: "))

    # Dictionaries for different languages
    lang = {
        "UZB": {
            "welcome": "O'zbek tili tanlandi.",
            "password_prompt": "Plastik karta paroli =>> ",
            "wrong_password": "Parol xato",
            "menu": [
                "Balans tekshirish",
                "Naqt pul olish",
                "SMS xabar ulash",
                "Parolni o'zgartirish",
                "Mobil aloqa uchun to'lov",
                "Kredit to'lovlar",
                "Komunal to'lovlar",
                "Dasturdan chiqish",
            ],
            "balance_check": "Balansingizda",
            "sum_left": "so'm mablag' bor.",
            "amount_left": "so'm qoldi.",
            "withdraw": [
                "50 000 so'm",
                "100 000 so'm",
                "150 000 so'm",
                "200 000 so'm",
                "300 000 so'm",
                "400 000 so'm",
                "Boshqa summa kiriting",
            ],
            "enter_sum": "Summa kiriting: ",
            "insufficient": "Mablag' yetarli emas.",
            "sms_options": ["SMS xabarni o'chirish", "SMS xabarni ulash"],
            "enter_phone": "Telefon raqamni kiriting (+998 bilan): ",
            "sms_disabled": " raqamdan SMS xabar o'chirildi.",
            "sms_enabled": " raqamga SMS xabar ulandi.",
            "mobile_payment": "Mobil aloqa uchun to'lov:",
            "operator_select": ["UzMobile", "Beeline", "Ucell", "UMS", "Perfectum"],
            "enter_amount": "To'lov summasini kiriting: ",
            "payment_successful": " to'lovi amalga oshirildi. Qolgan balans: ",
            "password_change": "Parolni o'zgartirish:",
            "password_old": "Joriy parolni kiriting: ",
            "password_new": "Yangi parol kiriting: ",
            "password_confirm": "Yangi parolni qayta kiriting: ",
            "password_changed": "Yangi parol muvaffaqiyatli o'rnatildi: ",
            "credit_prompt": "Kredit uchun to'lov summasini kiriting: ",
            "utility_prompt": "Komunal to'lov summasini kiriting: ",
            "exit": "Dasturdan chiqish",
        },
        "RUS": {
            "welcome": "Русский язык выбран.",
            "password_prompt": "Введите пароль пластиковой карты =>> ",
            "wrong_password": "Неправильный пароль",
            "menu": [
                "Проверить баланс",
                "Снять наличные",
                "Подключить SMS уведомление",
                "Изменить пароль",
                "Оплата мобильной связи",
                "Оплата кредита",
                "Коммунальные платежи",
                "Выход",
            ],
            "balance_check": "На вашем балансе",
            "sum_left": "сум.",
            "amount_left": "сум осталось.",
            "withdraw": [
                "50 000 сум",
                "100 000 сум",
                "150 000 сум",
                "200 000 сум",
                "300 000 сум",
                "400 000 сум",
                "Ввести другую сумму",
            ],
            "enter_sum": "Введите сумму: ",
            "insufficient": "Недостаточно средств.",
            "sms_options": ["Отключить SMS уведомление", "Подключить SMS уведомление"],
            "enter_phone": "Введите номер телефона (+998): ",
            "sms_disabled": " уведомление отключено.",
            "sms_enabled": " уведомление подключено.",
            "mobile_payment": "Оплата мобильной связи:",
            "operator_select": ["UzMobile", "Beeline", "Ucell", "UMS", "Perfectum"],
            "enter_amount": "Введите сумму для оплаты: ",
            "payment_successful": " оплачен успешно. Остаток на балансе: ",
            "password_change": "Изменение пароля:",
            "password_old": "Введите текущий пароль: ",
            "password_new": "Введите новый пароль: ",
            "password_confirm": "Подтвердите новый пароль: ",
            "password_changed": "Пароль успешно изменен: ",
            "credit_prompt": "Введите сумму для оплаты кредита: ",
            "utility_prompt": "Введите сумму коммунального платежа: ",
            "exit": "Выход из программы",
        },
        "ENG": {
            "welcome": "English language selected.",
            "password_prompt": "Enter your card PIN =>> ",
            "wrong_password": "Wrong PIN",
            "menu": [
                "Check Balance",
                "Withdraw Cash",
                "Activate SMS Alerts",
                "Change PIN",
                "Mobile Payment",
                "Credit Payments",
                "Utility Payments",
                "Exit",
            ],
            "balance_check": "Your balance is",
            "sum_left": "sum.",
            "amount_left": "sum left.",
            "withdraw": [
                "50 000 sum",
                "100 000 sum",
                "150 000 sum",
                "200 000 sum",
                "300 000 sum",
                "400 000 sum",
                "Enter another amount",
            ],
            "enter_sum": "Enter amount: ",
            "insufficient": "Insufficient funds.",
            "sms_options": ["Disable SMS alerts", "Activate SMS alerts"],
            "enter_phone": "Enter phone number (+998): ",
            "sms_disabled": " SMS alerts disabled for.",
            "sms_enabled": " SMS alerts activated for.",
            "mobile_payment": "Mobile Payment:",
            "operator_select": ["UzMobile", "Beeline", "Ucell", "UMS", "Perfectum"],
            "enter_amount": "Enter payment amount: ",
            "payment_successful": " payment successful. Remaining balance: ",
            "password_change": "Change PIN:",
            "password_old": "Enter current PIN: ",
            "password_new": "Enter new PIN: ",
            "password_confirm": "Re-enter new PIN: ",
            "password_changed": "PIN successfully changed: ",
            "credit_prompt": "Enter the credit payment amount: ",
            "utility_prompt": "Enter the utility payment amount: ",
            "exit": "Exit the program",
        },
    }

    # Determine the selected language
    lang_selected = "UZB" if til == 1 else "RUS" if til == 2 else "ENG"

    # Display welcome message
    print(lang[lang_selected]["welcome"])

    # Password check
    parol = int(input(lang[lang_selected]["password_prompt"]))

    if parol == parol1:
        while True:
            # Display menu
            for i, option in enumerate(lang[lang_selected]["menu"], 1):
                print(f"{i}. {option}")

            menyu = int(input("Select an option: "))

            # Menu options
            if menyu == 1:
                print(
                    f"{lang[lang_selected]['balance_check']} {mablag} {lang[lang_selected]['sum_left']}"
                )

            elif menyu == 2:
                print("\n".join(lang[lang_selected]["withdraw"]))
                naqt = int(input(lang[lang_selected]["enter_sum"]))
                if naqt <= mablag:
                    mablag -= naqt
                    print(
                        f"{lang[lang_selected]['balance_check']} {mablag} {lang[lang_selected]['amount_left']}"
                    )
                else:
                    print(lang[lang_selected]["insufficient"])

            elif menyu == 3:
                print(f"1. {lang[lang_selected]['sms_options'][0]}")
                print(f"2. {lang[lang_selected]['sms_options'][1]}")
                sms_option = int(input("Choose: "))
                tel = input(lang[lang_selected]["enter_phone"])
                if sms_option == 1:
                    print(f"{tel}{lang[lang_selected]['sms_disabled']}")
                else:
                    print(f"{tel}{lang[lang_selected]['sms_enabled']}")

            elif menyu == 4:
                print(lang[lang_selected]["password_change"])
                old_pin = int(input(lang[lang_selected]["password_old"]))
                if old_pin == parol1:
                    new_pin = int(input(lang[lang_selected]["password_new"]))
                    confirm_pin = int(input(lang[lang_selected]["password_confirm"]))
                    if new_pin == confirm_pin:
                        parol1 = new_pin
                        print(lang[lang_selected]["password_changed"], parol1)
                    else:
                        print("Error: PINs do not match.")
                else:
                    print(lang[lang_selected]["wrong_password"])

            elif menyu == 5:
                print(lang[lang_selected]["mobile_payment"])
                for i, operator in enumerate(lang[lang_selected]["operator_select"], 1):
                    print(f"{i}. {operator}")
                operator_choice = int(input("Select your operator: "))

                tel = input(lang[lang_selected]["enter_phone"])

                # Ask for the payment amount
                amount = int(input(lang[lang_selected]["enter_amount"]))

                # Check if sufficient balance is available
                if amount <= mablag:
                    mablag -= amount
                    print(
                        f"{lang[lang_selected]['operator_select'][operator_choice - 1]}{lang[lang_selected]['payment_successful']}{mablag} so'm"
                    )
                else:
                    print(lang[lang_selected]["insufficient"])

            elif menyu == 6:
                credit_amount = int(input(lang[lang_selected]["credit_prompt"]))
                if credit_amount <= mablag:
                    mablag -= credit_amount
                    print(
                        f"{lang[lang_selected]['balance_check']} {mablag} {lang[lang_selected]['amount_left']}"
                    )
                else:
                    print(lang[lang_selected]["insufficient"])

            elif menyu == 7:
                utility_amount = int(input(lang[lang_selected]["utility_prompt"]))
                if utility_amount <= mablag:
                    mablag -= utility_amount
                    print(
                        f"{lang[lang_selected]['balance_check']} {mablag} {lang[lang_selected]['amount_left']}"
                    )
                else:
                    print(lang[lang_selected]["insufficient"])

            elif menyu == 8:
                print(lang[lang_selected]["exit"])
                break

            else:
                print("Invalid option!")

    else:
        print(lang[lang_selected]["wrong_password"])


# Run the ATM program
atm()
