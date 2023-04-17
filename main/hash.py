import hashlib

def md5_hash(file_name):
    with open(file_name, 'rb') as f:
        bytes = f.read()
        md5hash = hashlib.md5(bytes).hexdigest()
        f.close()
    
    return md5hash

print(md5_hash("gui\main.py"))


def check_hash(file_path):
    file_hash = md5_hash(file_path)
    counter=0
    malware_hash = list(open("main\hash_key.txt", 'r').read().split("\n"))
    
    for i in malware_hash: 
        if i == file_hash:
            return "Malware Detected"
        counter+=1
    return "No Malware"
        
   
print(check_hash("gui\main.py"))