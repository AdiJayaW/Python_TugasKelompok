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

def save_data(all_data):
    try:
        with open(file_json, 'w') as file:
            json.dump(all_data, file, indent=4)
    except Exception as e:
        print (f"Gagal menyimpan data: {e}")

# ==========================================
# 2. BAGIAN BANTU BANTU
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
            account_angka = int(account_input)
            if len(account_input) != 3:
                print (f"Format Salah Akun Bank harus 3 digit")
                time.sleep(1)
                chance += 1
                continue

            password = input(f"Masukkan PIN ATM kamu (6 digit) : ")
            password_angka = int(password)       
            if len(password) != 6:
                print (f"Format Salah Akun Bank harus 3 digit")
                time.sleep(1)
                chance += 1
                continue 


            for user in database_user:
                if user['akun_bank'] == account_angka and user['pin'] == password_angka:
                    print (f"\nLogin Berhasil Selamat datang {user['nama']}")
                    time.sleep(1)
                    return user
            print("Akun atau Pin yang Anda masukkan salah, coba lagi")
            chance += 1
            time.sleep(1)


        except ValueError:
            print("❌ Input tidak valid. Kamu harus memasukkan angka.")
            chance += 1
            time.sleep(1)

        if chance > max_chance:
            print (f"Anda telah melakukan percobaan {max_chance} kali, coba ulangi beberapa saat lagi")    
            break
    return None

# ==========================================
# 4. BAGIAN TRANSAKSI 
# ==========================================
def check_balance(user):
    convert_balance = convert_uang(user['balance'])
    print(f"Saldo Anda saat ini adalah: {convert_balance}")
    time.sleep(1)

def deposit(user, all_data, amount):
    if amount > 0:
        user['balance'] += amount
        save_data(all_data)

        convert_amount = convert_uang(amount)
        convert_balance = convert_uang(user['balance'])
        print(f"Setor Tunai: {convert_amount}. Update Saldo: {convert_balance}")
    else:
        print("Deposit Gagal. Jumlah harus lebih dari 0.")
    time.sleep(1)


def withdraw(user, all_data, amount):
    if 0 < amount <= user['balance'] :
        user['balance'] -= amount
        save_data(all_data)
        convert_amount = convert_uang(amount)
        convert_balance = convert_uang(user['balance'])
        print(f"Tarik Tunai: {convert_amount}. Update Saldo: {convert_balance}")
    else:
        print("Penarikan Gagal. Periksa jumlah yang Anda masukkan dan saldo Anda.")
    time.sleep(1)

def transfer (user, all_data):
    while True:
        try:

            akun_orang = input("Masukkan Nomor Rekening Tujuan : ")
            try:
                rekening_tujuan = int(akun_orang)
            except ValueError:
                print("Inputan harus Berupan angka")
                continue

            penerima_ditemukan = None #Variabel untuk menyimpan data penerima jika ditemukan
            for data_orang in all_data:
                if data_orang['akun_bank'] == rekening_tujuan:
                        penerima_ditemukan = data_orang
                        break

            if penerima_ditemukan:
                if penerima_ditemukan['akun_bank'] == user['akun_bank']:
                    print("Gagal: Anda tidak bisa transfer ke rekening sendiri.")
                    time.sleep(1)
                    continue
                nama_penerima = penerima_ditemukan['nama']
                rekening_penerima =penerima_ditemukan['akun_bank']
                print(f"""
KONFIRMASI TRANSFER
Ke: {nama_penerima}
Rek: {rekening_penerima}

1. BENAR
2. SALAH
""")
                while True:
                    konfirmasi_akun = int(input("Masukkan Pilihan (1/2): "))
                    if konfirmasi_akun == 1 :
                        while True:
                            nominal = input(f"Masukkan nominal transfer untuk {nama_penerima}: ")
                            try :
                                nominal = int(nominal)
                            except:
                                print("Nominal tidak valid (harus angka). Silakan input ulang.")
                                continue # Kembali ke input nominal (Loop 2)
                            nominal_convert = convert_uang(nominal)
                            print(f"""
KONFIRMASI TRANSFER
Ke: {nama_penerima}
Jumalah Transfer : {nominal_convert}

1. BENAR
2. SALAH
""")
                            while True :
                                try:
                                    nominal_ask= int(input("Masukkan pilihan (1/2): "))
                                    if nominal_ask == 1:
                                        # --- EKSEKUSI TRANSFER DISINI ---
                                        print("Transfer SEDANG DIPROSES...")
                                        if user['balance'] >= nominal:
                                            user['balance'] -= nominal
                                            penerima_ditemukan['balance'] += nominal

                                            convert_balance = convert_uang(user['balance'])
                                            save_data(all_data)
                                            print(f"Transfer Berhasil! Sisa saldo anda: {convert_balance}")
                                            return
                                        else:
                                            convert_balance = convert_uang(user['balance'])
                                            print(f"Saldo tidak cukup Sisa saldo anda: {convert_balance}")
                                        # ...
                                        print("Transfer BERHASIL.")
                                        return # Selesai, keluar dari fungsi transfer
                                    elif nominal_ask == 2:
                                        print("Konfirmasi dibatalkan. Silakan masukkan nominal yang benar.")
                                        break
                                    else:
                                        print("Pilihan salah. Hanya 1 atau 2.")
                                        continue
                                except ValueError:
                                    print("Error: Masukkan angka saja!")
                    elif konfirmasi_akun == 2:
                        print(f"Permintaan transfer dibatalkan, Silahkan coba lagi")
                        break
        except ValueError:
            print("Input salah. Masukkan angka 1 atau 2.")
        else:
            print(f"Nomor Rekening {rekening_tujuan} tidak ditemukan, silahkan coba lagi")
            continue


    

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
0. Keluar
1. Cek Saldo
2. Setor Tunai
3. Tarik Tunai
4. Transfer
""")
        try:
            choice = input("Pilih opsi (0-4): ")
            choice_convert = int(choice)

            # Mendeklarasikan agar opsi 1 dan 4 mereset counter spam menjadi 0, agar tidak dihitung kemudian menjadi 1 lagi.
            if 0<= choice_convert <= 4:
                counter_spam = 0

                if choice_convert == 0:
                    print("Terima kasih telah menggunakan Layanan ATM Sederhana, Adios Mabroo!")
                    break
                elif choice_convert == 1: #jika pilih angka "1", maka akan masuk ke fungsi check_balance
                    check_balance(current_users)
                elif choice_convert == 2: #jika pilih angka "2", maka bisa memasukkan nilai ke variabel amount, lalu nilai tersebut dibuat parameter, ketika fungsi deposit dijalankan.
                    amount = int(input("Masukkan jumlah yang akan disetorkan dalam bentuk rupiah: "))
                    deposit(current_users, database_users, amount)
                elif choice_convert == 3:
                    amount = int(input("Masukkan jumlah yang akan ditarik dalam bentuk rupiah: "))
                    withdraw(current_users, database_users, amount)
                elif choice_convert == 4:
                    transfer(current_users, database_users)
            else :
                print("❌ Pilihan tidak valid. Silahkan coba lagi.")
                time.sleep (0.8)

            if counter_spam >= max_spam:
                print (f"Anda telah melakukan percobaan {max_spam} kali, coba ulangi beberapa saat lagi")
                break

        except ValueError :
            print("❌ Input tidak valid. Kamu harus memasukkan angka.")
            counter_spam += 1
            print(f"Peringatan Spam: {counter_spam}/{max_spam}")
            time.sleep (1)

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