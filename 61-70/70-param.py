
def sum_row(a,k, m,n):
    if k > m:
        return 0
    else:
        return sum(a[k-1])
    

m = int(input("qatorlar sonini kiriting (m)"))
n = int(input("ustunlar sonini kiriting (n)"))

print(f"{m}x{n} matrisa element qatorma qator kiriting ")
a = []
for i in range(m):
    row = list(map(int, input(f"{i+1}-qator uchun {n}ta elemen kiriting").split()))
    a.append(row)

k = int(input("Yigindisni (K)"))

print(f"Yigindisi: {sum_row(a,k,m,n)}")
