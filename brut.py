from rarfile import RarFile, Error

passwords = ['1234', 'password', 'admin', '1111']

with RarFile('secrets.rar') as rf:
    for pwd in passwords:
        rf.setpassword(pwd)
        try:
            rf.extractall()
            print('Found password!!!: ', pwd)
            break
        except Error:
            print("Invalid variant: ", pwd)
