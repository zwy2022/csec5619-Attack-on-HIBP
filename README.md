# CSEC5619-Attack-on-HIBP
- Run 'get_pwned_pwd.py' first, enter password 1 you want to check. Then the retrieved hash values will be stored in 'hashes' directory.
- Copy every file's content in 'hashes' directory to "https://md5decrypt.net/en/Sha1/" to get decrypted plaintext. Over write and copy plaintexts to 'pt1.txt'.
- Delete 'hashes' directory, repeat the above procedures, but copy copy plaintexts to 'pt2.txt'.
- Run 'compare.py' to get the final attack result of whether there are password pairs with same prefix that will be potential user input.

