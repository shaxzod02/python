

def sum_column(a,k, m,n):
    if k >= n:
        return 0
    else:
        column_sum = 0
        for i in range(m):
            column_sum += a[i][k]
        return column_sum
    

m = int(input("qatorlar sonini kiriting (m)"))
n = int(input("ustunlar sonini kiriting (n)"))

print(f"{m}x{n} matrisa element qatorma qator kiriting ")
a = []
for i in range(m):
    row = list(map(int, input(f"{i+1}-qator uchun {n}ta elemen kiriting").split()))
    a.append(row)

k = int(input("Yigindisni (K)"))

print(f"Yigindisi: {sum_column(a,k,m,n)}")
