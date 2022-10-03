import hashlib

def get_int64_hash(string: str):
    hash_obj = hashlib.sha256(string.encode('utf-8')) 
    int_hash = int(hash_obj.hexdigest(), base=16) % 10**64
    return int_hash