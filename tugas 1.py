# #program membuat volume balok
panjang_balok = int(input("masukkan panjang balok: "))
print(panjang_balok, "bertipe", type(panjang_balok))

lebar_balok = int(input("masukkan lebar balok:"))
print(lebar_balok, "bertipe", type(lebar_balok))

tinggi_balok = int(input("masukkan tinggi balok: "))
print(lebar_balok, "bertipe", type(lebar_balok))

V = panjang_balok  * lebar_balok * tinggi_balok
print("rumus menghitung volume balok", panjang_balok * lebar_balok  * tinggi_balok)
print("hasil dari volume balok: ",V)

