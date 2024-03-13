import hashlib, time
import plotly.graph_objects as go


#Hash function with following param. Function includes time counting
def Hash(sample, hash_type):
    start_time = time.time()
    hash_algorithms = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512,
        'blake2b': hashlib.blake2b,
        'blake2s': hashlib.blake2s,
        'sha3_224': hashlib.sha3_224,
        'sha3_256': hashlib.sha3_256,
        'sha3_384': hashlib.sha3_384,
        'sha3_512': hashlib.sha3_512,
        'shake128': hashlib.shake_128,
        'shake256': hashlib.shake_256
    }
    if hash_type not in hash_algorithms:
        raise ValueError("Invalid hash type")

    h = hash_algorithms[hash_type]()
    h.update(sample)

    if hash_type in ['shake128', 'shake256']:
        result = h.hexdigest(16 if hash_type == 'shake128' else 32)
    else:
        result = h.hexdigest()
    end_time = time.time()
    xtime = end_time - start_time
    return result,xtime


# DATA
file_path = './text'

with open(file_path, "rb") as file:
    sample = file.read()

hash_types = ['sha224', 'sha256', 'sha384', 'sha512', 'md5', 'blake2b', 'blake2s',
              'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'shake128', 'shake256']

# Result for each hash type with diagram

hashed_values = []
time_results = []

for hash_type in hash_types:
    hashed, time_result = Hash(sample, hash_type)

    hashed_values.append(hashed)
    time_results.append(time_result)

    print("Time result for {}: {:.6f} seconds, Hash: {}".format(hash_type, time_result, hashed))


fig = go.Figure(data=go.Bar(x=list(hash_types), y=list(time_results)))
fig.update_layout(title='Time of generated data for every hash_type',
                  xaxis_title='Hash Type',
                  yaxis_title='Time (Sec)')
fig.show()