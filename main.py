import time
import json
import os

file_json = 'user.json'

# ==========================================
# 1. BAGIAN DATA (Load & Save)
# ==========================================
def load_data():
    if not os.path.exists(file_json):
        return []
    try:
        with open (file_json, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


# ==========================================
# 2. BAGIAN HELPER
# ==========================================
def convert_uang(angka):
    hasil_awal = f"Rp {angka:,.0f}"
    hasil_akhir = hasil_awal.replace(',', '.')

    return hasil_akhir


# ==========================================
# 3. BAGIAN AUTH (Login)
# ==========================================
def login(database_user):
    chance = 1
    max_chance = 3

    while (chance <= max_chance):

        try:
            print(f"\n--- Percobaan Login ke-{chance} dari {max_chance} ---")
            print(f"""
"Selamat Pagi", Selamat datang di Simulasi ATM SDERHANAAAAA!!!!

Silahkan Masukkan Akun Bank Beserta Pinnya 
""")
    
            account_input = input(f"Masukkan Akun Bank kamu (3 digit) : ")
            if len(account_input) != 3:
                print (f"Format Salah Akun Bank harus 3 digit")
                time.sleep(0.8)
                continue

            password = input(f"Masukkan PIN ATM kamu (6 digit) : ")       
            if len(password) != 6:
                print (f"Format Salah Akun Bank harus 3 digit")
                time.sleep(0.8)
                continue 

            account_angka = int(account_input)
            password_angka = int(password)

            for user in database_user:
                if user['akun_bank'] == account_angka and user['pin'] == password_angka:
                    print (f"\nLogin Berhasil Selamat datang {user['nama']}")
                    time.sleep(0.9)
                    return user
            print("Akun atau Pin yang Anda masukkan salah, coba lagi")
            chance += 1

        except ValueError:
            print("❌ Input tidak valid. Kamu harus memasukkan angka.")
            chance += 1

        if chance > max_chance:
            print (f"Anda telah melakukan percobaan {max_chance} kali, coba ulangi beberapa saat lagi")    
            break
    return None

# ==========================================
# 4. BAGIAN TRANSAKSI (YANG DIPERBAIKI)
# ==========================================
def check_balance(user):
    convert_balance = convert_uang(user['balance'])
    print(f"Saldo Anda saat ini adalah: {convert_balance}")
    time.sleep(2)

def deposit(amount):
    if amount > 0:
        balance += amount
        convert_amount = convert_uang(amount)
        convert_balance = convert_uang(balance)
        print(f"Setor Tunai: {convert_amount}. Update Saldo: {convert_balance}")
    else:
        print("Deposit Gagal. Jumlah harus lebih dari 0.")
    time.sleep(1.8)


def withdraw(amount):
    if 0 < amount <= balance :
        balance -= amount
        convert_amount = convert_uang(amount)
        convert_balance = convert_uang(balance)
        print(f"Tarik Tunai: {convert_amount}. Update Saldo: {convert_balance}")
    else:
        print("Penarikan Gagal. Periksa jumlah yang Anda masukkan dan saldo Anda.")
    time.sleep(1.8)






def main_menu(current_users, database_users):
    counter_spam = 0
    max_spam = 3
    print(f""" 
========================================|
Selamat Datang di Simulasi ATM Sederhana|
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
        try:
            choice = input("Pilih opsi (1-4): ")
            choice_convert = int(choice)

            # Mendeklarasikan agar opsi 1 dan 4 mereset counter spam menjadi 0, agar tidak dihitung kemudian menjadi 1 lagi.
            if 1<= choice_convert <= 4:
                counter_spam = 0

                if choice_convert == 1: #jika pilih angka "1", maka akan masuk ke fungsi check_balance
                    check_balance(current_users)
                elif choice_convert == 2: #jika pilih angka "2", maka bisa memasukkan nilai ke variabel amount, lalu nilai tersebut dibuat parameter, ketika fungsi deposit dijalankan.
                    amount = int(input("Masukkan jumlah yang akan disetorkan dalam bentuk rupiah: "))
                    deposit(amount)
                elif choice_convert == 3:
                    amount = int(input("Masukkan jumlah yang akan ditarik dalam bentuk rupiah: "))
                    withdraw(amount)
                elif choice_convert == 4:
                    print("Terima kasih telah menggunakan Layanan ATM Sederhana, Adios Mabroo!")
                    break
            else :
                print("❌ Pilihan tidak valid. Silahkan coba lagi.")
                counter_spam += 1
                print(f"Peringatan Spam {counter_spam}/{max_spam}")
                time.sleep (0.8)

            if counter_spam >= max_spam:
                print (f"Anda telah melakukan percobaan {max_spam} kali, coba ulangi beberapa saat lagi")
                break

        except ValueError :
            print("❌ Input tidak valid. Kamu harus memasukkan angka.")
            counter_spam += 1
            print(f"Peringatan Spam: {counter_spam}/{max_spam}")
            time.sleep (0.8)

            if counter_spam >= max_spam:
                print (f"Anda telah melakukan percobaan {max_spam} kali, coba ulangi beberapa saat lagi")    
                break    

        except Exception as e:
            print(f"⚠️ Terjadi kesalahan tak terduga: {e}")
            break


# --- Menjalankan Program ---
if __name__ == "__main__":
    database_users = load_data()
    current_user = login(database_users)
    if current_user is not None:
        main_menu(current_user, database_users)