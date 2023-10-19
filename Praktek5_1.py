nilai = input("masukkan nilai: ").upper()
isi = []

while 1 == 1:
    if nilai == "A":
        isi.append(4.00)
        print("A = 4.00")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "A-":
        isi.append(3.75)
        print("A- = 3.75")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "B+":
        isi.append(3.50)
        print("B+ = 3.50")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "B":
        isi.append(3.00)
        print("B = 3.00")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "B-":
        isi.append(2.75)
        print("B- = 2.75")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "C+":
        isi.append(2.50)
        print("C+ = 2.50")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "C":
        isi.append(2.00)
        print("C = 2.00")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "C-":
        isi.append(1.75)
        print("C- = 1.75")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "D":
        isi.append(1.50)
        print("D = 1.50")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "E":
        isi.append(1.25)
        print("E = 1.25")
        nilai = input("masukkan nilai: ").upper()
    elif nilai == "":
        rata2 = sum(isi) / len(isi)
        print(rata2)
        break
    else:
        print("masukkan nilai dengan benar")
        nilai = input("masukkan nilai: ").upper()