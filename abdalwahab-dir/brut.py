from rarfile import RarFile
from rarfile import Error, BadRarFile
import string
import itertools
from time import sleep

alp = "om" + string.ascii_lowercase

with RarFile('/home/kali/mohammed-repo/secrets.rar') as rf:
    for var in itertools.product(alp, repeat=4):
        pwd = ''.join(var)
        rf.setpassword(pwd)
        try:
            rf.extractall()
            print('Found password!!!: ', pwd)
            break
        except BadRarFile as e:
            print("Invalid variant : ", pwd)
