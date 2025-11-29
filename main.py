import time
balance = 0

def main():
    print(""" 
    ========================================|
    Selamat Datang di Simulasi ATM SEDERHANA|
           Bersama dengan Adi dan Jefry     |
    ========================================|
    

""")
    while True:
        print("\nMenu:")
        print("""
1. Cek Saldo
2. Setor Tunai
3. Tarik Tunai
4. Keluar
""")
        choice = int(input("Pilih opsi (1-4): "))

        # Fungsi untuk Memilih Opsi dari Menu yang tersedia

        if choice == 1:
            check_balance()
        elif choice == 2:
            amount = int(input("Masukkan jumlah yang akan disetorkan dalam bentuk rupiah: "))
            deposit(amount)
        elif choice == 3:
            amount = int(input("Masukkan jumlah yang akan ditarik dalam bentuk rupiah: "))
            withdraw(amount)
        elif choice == 4:
            print("Terima kasih telah menggunakan Layanan ATM Sederhana, Adios Mabroo!")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

def check_balance():
    print(f"Saldo Anda saat ini adalah: {balance}")
    time.sleep(2)

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Setor Tunai: {amount}. Update Saldo: {balance}")
    else:
        print("Deposit Gagal. Jumlah harus lebih dari 0.")
    time.sleep(1.8)

def withdraw(amount):
    global balance 
    if 0 < amount <= balance :
        balance -= amount
        print(f"Tarik Tunai: {amount}. Update Saldo: {balance}")
    else:
        print("Penarikan Gagal. Periksa jumlah yang Anda masukkan dan saldo Anda.")
    time.sleep(1.8)


# --- Menjalankan Program ---
if __name__ == "__main__":
    main()