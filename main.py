import os

folder_path = "C:/Users/YourName/Desktop/files"

files = os.listdir(folder_path)

for i, file in enumerate(files, start=1):
    old_path = os.path.join(folder_path, file)
    new_name = f"file_{i}.txt"
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

print("Renaming completed!")