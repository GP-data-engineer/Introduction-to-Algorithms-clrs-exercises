import os

# Nazwy plików, których szukamy
TARGET_FILES = {"_git_for_windows.updater", "_pdfbox.cache"}

def find_target_files():
    start_dir = os.path.dirname(os.path.abspath(__file__))
    found_files = []

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file in TARGET_FILES:
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    if found_files:
        print("✅ Znalezione pliki:")
        for path in found_files:
            print(path)
    else:
        print("ℹ Nie znaleziono żadnego z plików.")

if __name__ == "__main__":
    find_target_files()

