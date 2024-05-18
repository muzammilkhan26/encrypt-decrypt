from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()

key_folder = "/Folder/Path" # Enter folder path to save key.

key_file_path = os.path.join(key_folder, "mykey.key")
with open(key_file_path, "wb") as key_file:
    key_file.write(key)

f = Fernet(key)

folder_path = "/Folder/Path"  # Enter folder path to Encrypt.

files = os.listdir(folder_path)

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path): 
        with open(file_path, "rb") as o_r:
            original = o_r.read()
            encrypted = f.encrypt(original)
        with open(file_path, "wb") as o_w:
            o_w.write(encrypted)

print("Encryption Complete!")