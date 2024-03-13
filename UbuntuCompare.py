import hashlib

def Ubuntu(path):
    """
    Verifies the integrity of an Ubuntu ISO file by comparing its SHA256 hash.

    Parameters:
        path (str): The path to the Ubuntu ISO file.

    Returns:
        str: 'true' if the hash matches the expected value, 'false' otherwise.
    """
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            h.update(data)

    if h.hexdigest() == '071d5a534c1a2d61d64c6599c47c992c778e08b054daecc2540d57929e4ab1fd':
        result = 'true'
    else:
        result = 'false'
    return result

# Path to destination file
file_path = './ubuntu-22.04.4-desktop-amd64.iso'
# Compare calculated_Hash_of_ISO
print('Compare hashed iso file : ', Ubuntu(file_path))
