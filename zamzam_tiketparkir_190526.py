print("selamat datang di Parkirmu!")

zami = 1
while zami < 10:
    zamp = int(input("berapa jam anda parkir?"))
    if zamp == 0:
        print("nominal parkir : 0")
        break

    if zamp <= 2:
        zamh = 3000

    elif zamp > 2:
        zamh = 3000 + (zamp - 2) * 2000
    print("nominal parkir", zamh)



