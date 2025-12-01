from rarfile import RarFile, BadRarFile

passwords = ['1234', 'password', 'admin', '1111']

with RarFile('secrets.rar') as rf:
    for pwd in passwords:
        rf.setpassword(pwd)
        try:
            rf.extractall()
            print('Found password!!!: ', pwd)
            break
        except BadRarFile:
            print("Invalid variant: ", pwd)
