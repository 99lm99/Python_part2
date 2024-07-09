import os
import json
import csv
import pickle

def get_directory_info(directory):
    directory_info = []

    def get_size(start_path='.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def walk_dir(current_directory, parent_directory=""):
        try:
            with os.scandir(current_directory) as it:
                for entry in it:
                    if entry.is_file():
                        file_info = {
                            "name": entry.name,
                            "path": entry.path,
                            "parent_directory": parent_directory,
                            "type": "file",
                            "size": entry.stat().st_size
                        }
                        directory_info.append(file_info)
                    elif entry.is_dir():
                        dir_info = {
                            "name": entry.name,
                            "path": entry.path,
                            "parent_directory": parent_directory,
                            "type": "directory",
                            "size": get_size(entry.path)
                        }
                        directory_info.append(dir_info)
                        walk_dir(entry.path, entry.path)
        except PermissionError:
            pass  # Ignore directories that cannot be accessed

    walk_dir(directory)
    return directory_info

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

# Использование функций
directory = "your_directory_path_here"
directory_info = get_directory_info(directory)

save_to_json(directory_info, "directory_info.json")
save_to_csv(directory_info, "directory_info.csv")
save_to_pickle(directory_info, "directory_info.pkl")
