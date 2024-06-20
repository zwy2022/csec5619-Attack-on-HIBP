import re

def extract_passwords(file_path):
    passwords = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r': (.*)', line)
            if match:
                password = match.group(1).strip()
                passwords.append(password)
    return passwords
def find_common_prefix_pairs(passwords1, passwords2):
    similar_password_pairs = []
    for pwd1 in passwords1:
        for pwd2 in passwords2:
            common_prefix = get_common_prefix(pwd1, pwd2)
            if common_prefix:
                similar_password_pairs.append((pwd1, pwd2))
    return similar_password_pairs

def get_common_prefix(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            return str1[:i] if i > 5 else None
    return str1[:min_length]

passwords_pt1 = extract_passwords('pt1.txt')
passwords_pt2 = extract_passwords('pt2.txt')

similar_password_pairs = find_common_prefix_pairs(passwords_pt1, passwords_pt2)

print("Password pairs with common prefix found:")
for pair in similar_password_pairs:
    print(pair)
