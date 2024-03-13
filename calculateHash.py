import hashlib

def calculate_hash(file_path, buffer_size):
    """
    Calculates the hash of a file using the SHA256 algorithm.

    Parameters:
        file_path (str): The path to the file.
        buffer_size (int): The size of the buffer used for reading the file.

    Returns:
        str: The hexadecimal representation of the file's SHA256 hash.
    """
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            h.update(data)

    return h.hexdigest()

# Path to example file
file_path = './ubuntu-22.04.4-desktop-amd64.iso'

# Result of hashed file
print('Hashed file: ', calculate_hash(file_path, 4096))
