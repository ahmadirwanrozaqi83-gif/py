def penjumblahan(a,b):
    print(f"{a} + {b} = {a+b}")


def pengurangan(a,b):
    print(f"{a} - {b} = {a-b}")


def pembagian(a,b):
    print(f"{a} / {b} = {a/b}")


def perkalian(a,b):
    print(f"{a} * {b} = {a*b}")


status = True

while status:
    print("="*20)
    print("Kalkulator".center(20))
    print("="*20)
    print()
    print("Pilih opsi:")
    print()
    print("1. Penjumlahan")
    print("2. Pengurangan ")
    print("3. Pembagian")
    print("4. Perkalian")
    print("5. Exit")
    print("="*20)

    opsi = (input("Pilih opsi :"))

    if opsi == "5":
        print("kamu keluar syuhh")
        status = False

    elif opsi in ("1", "2", "3", "4"):

        num1 = int(input("Masukan angka pertama :"))
        num2 = int(input("Masukan angka kedua :"))

        if opsi == "1":
            print(f"{penjumblahan(num1,num2)}")
        
        elif opsi == "2":
            print(f"{pengurangan(num1,num2)}")
        
        elif opsi == "3":
            print(f"{pembagian(num1,num2)}")
        
        elif opsi == "4":
            print(f"{perkalian(num1,num2)}")


