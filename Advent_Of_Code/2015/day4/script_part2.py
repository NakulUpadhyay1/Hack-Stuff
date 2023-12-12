import hashlib

secret_key = 'yzbqklnj'
counter = 0

while True:
    input_string = secret_key + str(counter)
    encoded_hash = hashlib.md5(input_string.encode())
    generated_hash = encoded_hash.hexdigest()

    if generated_hash.startswith('000000'):
        print(f"Found hash with 5 leading zeros: {generated_hash}")
        print(f"Counter value: {counter}")
        break

    counter += 1


