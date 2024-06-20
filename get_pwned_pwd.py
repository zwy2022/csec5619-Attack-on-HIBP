import requests
import os
import hashlib
def compute_sha1(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    sha1_hash = sha1.hexdigest()
    return sha1_hash

# Get pwned passwords from HIBP
def get_pwned_passwords(prefix):
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code}"

# Create dictionary to store data

def parse_pwned_passwords_response(response_text, prefix):
    result_list = []

    lines = response_text.splitlines()

    for line in lines:
        suffix, _ = line.split(':')
        full_hash = prefix + suffix
        result_list.append(full_hash)

    return result_list

# Store ciphertexts in different files,
# with each file containing a group of 100 items.
def save_hashes_to_files(hashes, directory="hashes"):
    os.makedirs(directory, exist_ok=True)

    for i in range(0, len(hashes), 100):
        batch = hashes[i:i + 100]
        file_name = os.path.join(directory, f'hashes_{i // 100 + 1}.txt')
        with open(file_name, 'w') as f:
            for hash_value in batch:
                f.write(hash_value + '\n')
input_string = input("Please the password you want to check: \n").strip()
sha1_hash = compute_sha1(input_string)
prefix=sha1_hash[:5]
response_text = get_pwned_passwords(prefix)
result_list = parse_pwned_passwords_response(response_text, prefix)
save_hashes_to_files(result_list)
print("Please check the hashes directory for cipher results.\n");
