import hashlib
import os

malware_hash = list(open("main\hash_key.txt", 'r').read().split("\n"))
malware_name = list(open("main\hash_name.txt", 'r').read().split("\n"))


def sha256_file(file_name):
    with open(file_name, 'rb') as f:
        bytes = f.read()
        sha256hash = hashlib.sha256(bytes).hexdigest()
        f.close()

    return sha256hash

# Deep scanning for finding


def sha256_folder(folder_path):

    files = []
    dir_list = list()
    for (dir_path, dir_name, file_name) in os.walk(folder_path):
        dir_list += [os.path.join(dir_path, file) for file in file_name]

    for dir in dir_list:
        if sha256_file(dir) != 0:
            files.append(sha256_file(dir) + ":: FILE :: " + dir)
    print(*files, sep="\n")


# Checking for malware or virus in a single file
def file_scanner(file_path):
    file_hash = sha256_file(file_path)
    global malware_hash
    counter = 0

    # checking each file
    for hash in malware_hash:
        if hash == file_hash:
            return malware_name[counter]
        counter += 1
    return "No Malware"


virus_file_name = []
virus_file_path = []
# Checking for malware of virus in folder


def folder_scanner(folder_path):

    directory_list = list()

    # for deep scanning
    for (dir_path, dir_name, file_name) in os.walk(folder_path):
        directory_list += [os.path.join(dir_path, file) for file in file_name]

    # checking each file
    for dir in directory_list:
        if file_scanner(dir) != 0:
            if file_scanner(dir) != "No Malware":
                virus_file_name.append(
                    "|| Virus : " + file_scanner(dir) + " || File : " + dir)
                virus_file_path.append(dir)
    print(*virus_file_name, sep="\n")


def virus_remover(path):
    folder_scanner(path)
    if virus_file_path:
        for virus in virus_file_path:
            os.remove(virus)
    else:
        return 0


def junk_remover():

    temp_list = list()

    username = os.environ.get('USERNAME').upper().split(" ")
    print(username)
    for (dirpath, dirname, filename) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filename]
        temp_list += [os.path.join(dirpath, file) for file in dirname]
    for (dirpath, dirname, filename) in os.walk(f"C:\\Users\\{username[0]}~1\\AppData\\Local\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filename]
        temp_list += [os.path.join(dirpath, file) for file in dirname]
    for (dirpath, dirname, filename) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filename]
        temp_list += [os.path.join(dirpath, file) for file in dirname]
    if temp_list:
        for i in temp_list:
            print(i)
            try:
                print(f"Safely Deleted: {i}")
                os.remove(i)
            except:
                print(f"Unable To Delete: {i}")
            try:
                print(f"Safely Deleted: {i}")
                os.rmdir(i)
            except:
                print(f"Unable To Delete: {i}")
    else:
        return 0


def ram_booster():

    task_list = ["notepad.exe"]

    for task in task_list: 
        try:       
            os.system(f"taskkill /f /im {task}")
        except:
            pass