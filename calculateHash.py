import hashlib

def calculate_hash(file_path,buffer_size):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            h.update(data)

    return h.hexdigest()

# Path to Ubuntu file
file_path = './ubuntu-22.04.4-desktop-amd64.iso'

# Result of hashed file
print('Hashed file: ', calculate_hash(file_path,4096))