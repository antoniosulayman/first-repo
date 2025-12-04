from rarfile import RarFile, Error, BadRarFile
import string
import itertools


alp = "om" + string.ascii_lowercase


with RarFile('/home/kali/mohamed-repo/secrets.rar') as rf:
       pwd = ''.join(var)
        rf.setpassword(pwd)
        try:
            rf.extractall()
            print('Found password!!!:', pwd)
            break
        except Error:
            print("Invalid variant:", pwd)
