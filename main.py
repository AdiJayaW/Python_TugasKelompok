import time
import json

file_json = 'user.json'

try:
    with open (file_json, 'r') as file:
        data_user = json.load(file)

        username = data_user['nama']
        account = data_user["akun_bank"]
        pin = data_user["pin"]
        balance = data_user["balance"]

except FileNotFoundError:
    print(f"Error: File '{file_json}' tidak ditemukan. Pastikan file ada.")
    exit()
except json.JSONDecodeError:
    print(f"Error: Format File '{file_json}' salah ")

balance = 0
counter_spam = 0
max_spam = 3

def main():
    global counter_spam
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
                    check_balance()
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


def login():
    chance = 1
    max_chance = 3
    while (chance <= max_chance):
        try:
            print(f"\n--- Percobaan Login ke-{chance} dari {max_chance} ---")
            print(f"""
Halo {username}, Selamat datang di Simulasi ATM SDERHANAAAAA!!!!
""")
            account_input = input(f"Masukkan Akun Bank kamu (12 digit) : ")
            password = input(f"Masukkan PIN ATM kamu (6 digit) : ")
            account_angka = int(account_input)
            password_angka = int(password)
            if password_angka == pin and account_angka == account :
                print (f"Login Berhasil Selamat datang {username}")
                time.sleep(0.7)
                return True
            else:
                print (f"❌ account atau pin yang kamu masukkan salah")
                chance += 1

        except ValueError:
            print("❌ Input tidak valid. Kamu harus memasukkan angka.")
            chance += 1

            if chance > max_chance:
                print (f"Anda telah melakukan percobaan {max_chance} kali, coba ulangi beberapa saat lagi")    
                break    

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
    if login():
        main()