import hashlib

malware_hash = list(open("main\hash_key.txt", 'r').read().split("\n"))
malware_name = list(open("main\hash_name.txt", 'r').read().split("\n"))
def md5_hash(file_name):
    with open(file_name, 'rb') as f:
        bytes = f.read()
        md5hash = hashlib.sha256(bytes).hexdigest()
        f.close()
    
    return md5hash

print(md5_hash("gui\main.py"))


def check_hash(file_path):
    file_hash = md5_hash(file_path)
    global malware_hash
    counter = 0
    for i in malware_hash: 
        if i == file_hash:
            print("MALWARE DETECTED")
            return malware_name[counter]
        counter += 1
    return "No Malware"
        
   
print(check_hash("gui\main.py"))