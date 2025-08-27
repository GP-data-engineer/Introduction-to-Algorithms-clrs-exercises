import os

def rename_py_files_in_current_directory():
    # Katalog, w którym znajduje się ten skrypt
    current_dir = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(current_dir):
        old_path = os.path.join(current_dir, filename)

        # Pomijamy katalogi
        if os.path.isdir(old_path):
            continue

        # Bierzemy tylko pliki .py, ale pomijamy sam skrypt
        if not filename.lower().endswith(".py"):
            continue
        if filename == os.path.basename(__file__):
            continue

        # Rozdzielamy nazwę i rozszerzenie
        name, ext = os.path.splitext(filename)

        # Zamieniamy . i - na _
        new_name = name.replace('.', '_').replace('-', '_') + ext

        new_path = os.path.join(current_dir, new_name)

        # Zmieniamy nazwę tylko jeśli jest inna
        if old_path != new_path:
            try:
                os.rename(old_path, new_path)
                print(f"✅ Zmieniono: {filename}  →  {new_name}")
            except PermissionError:
                print(f"⚠ Nie można zmienić: {filename} (plik używany przez system)")

if __name__ == "__main__":
    rename_py_files_in_current_directory()