A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))


while B!= 0:
    A, B = B, A % B

print(f"Uchun eng katta umumiy bo'luvchi {A} ga teng")