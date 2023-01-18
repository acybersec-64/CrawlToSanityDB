import os

with open("cookie.txt") as ReadCookie:
    cookie = ReadCookie.read()

print("downloading Codes...\n\n---------------------------------------------------------------------------------")

os.system("python downloadCodes.py")

print("""\n\ndownloading Pages...\n\n---------------------------------------------------------------------------------""")

os.system('python downloadPages.py "{}" '.format(cookie))

print("\n\nRunning Occuptaion.py..\n\n---------------------------------------------------------------------------------")

os.system("python occupation.py")