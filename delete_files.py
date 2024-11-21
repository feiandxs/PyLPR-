import os

files_to_delete = [
    "注释 .txt",
    "部署文档 .txt"
]

for file in files_to_delete:
    try:
        os.remove(file)
        print(f"Deleted {file}")
    except FileNotFoundError:
        print(f"File {file} not found")
    except Exception as e:
        print(f"Error deleting {file}: {e}")
