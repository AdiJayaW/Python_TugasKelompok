import os
import json

# print(f"Script sedang dijalankan dari direktori: {os.getcwd()}")

file_json = 'user.json'

try:
    # 1. Buka file, mendapatkan objek file ('file')
    with open(file_json, 'r') as file:
        
        # 2. Gunakan json.load() (tanpa 's')
        #    'file' adalah objek file yang bisa dibaca.
        user = json.load(file) 
    
    print("Data berhasil dimuat:")
    print(user)

except FileNotFoundError:
    print("Error: File tidak ditemukan.")
except json.JSONDecodeError as e:
    print(f"Error: Format JSON tidak valid. Detail: {e}")