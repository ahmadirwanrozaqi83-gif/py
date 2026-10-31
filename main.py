siswa = ["andi","budi","alex"]

for nama in siswa :
    nilai_mtk =int(input("nilai_mtk="+ nama + ":"))
    nilai_bina =int(input("nilai_bina="+ nama + ":"))
    nilai_bing =int(input("nilai_bing="+ nama + ":"))

total_nilai_mapel = nilai_mtk + nilai_bina + nilai_bing
rata_rata = total_nilai_mapel / 3
print("rata rata nilai",rata_rata)