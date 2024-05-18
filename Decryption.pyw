from cryptography.fernet import Fernet
import os

key_file_path = "/Key/Path"  # Enter the folder path where the key is saved.

with open(key_file_path, "rb") as key_file:
    key = key_file.read()

f = Fernet(key)

folder_path = "/Folder/Path" # Enter folder path to Decrypt

files = os.listdir(folder_path)

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path): 
        with open(file_path, "rb") as o_r:
            encrypted = o_r.read()
            decrypted = f.decrypt(encrypted)
        with open(file_path, "wb") as o_w:
            o_w.write(decrypted)

print("Decryption complete!")
