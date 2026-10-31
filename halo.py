import random
angka_rahasia= 4
kesempatan = 0
while angka_rahasia:
    tebak=random.randint(1, 25)
    if kesempatan >= 5:
        print("kesempatan habiss")
        print ("Kamu kalahh!!!!")
        break
    if tebak == angka_rahasia:
        print( "Tebakan:", tebak)
        print("===============")
        print("Tebakan benarr!!")
        print("===============")
        kesempatan += 1
        print("kesempatan ke-", kesempatan)
        print("Kamu menanggg!!")
        break
    elif tebak > angka_rahasia:
        print("Tebakan:",tebak)
        print("terlalu besar, ulangi lagii") 
        kesempatan += 1
        print("kesempatan ke-", kesempatan)
        print()
    else:
        print("Tebakan:", tebak)
        print("terlalu kecil, ulangiii")
        kesempatan += 1
        print("kesempatan ke-", kesempatan)
        print()