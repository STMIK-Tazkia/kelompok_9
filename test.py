
# Soal nomor 1. Buatlah program untuk menghitung perkalian matrix
# Perkalian Matrixs 4x4
matriksC = [
    [90, 55, 34, 17],
    [33, 5, 75, 13],
    [14, 17, 21, 33],
    [33, 88, 7, 15],
]

matriksD =[
    [1, 1, 1, 1],
    [0, 1, 0,0],
    [0, 0, 1, 0],
    [1, 1, 1, 1]
]

#Perkalian matriks
hasil = [[sum(matriksC[i][k] * matriksD[k][j] for k in range (4)) for j in range (4)] for i in range(4)]

#Menampilkan hasil perkalian
print("Hasil perkalian matriks:")
for baris in hasil:
    print(baris)




#Soal nomor 2. Buatlah fungsi untuk mengambil irisan dan beda setangkup dari dua himpunan ini 
#Definisi himpunan C dan D
A ={37, 41, 50, 16, 22, 300, 5, 14, 3, 120, 45}
B ={41, 120, 56, 17, 21, 3, 50, 15, 6, 4, 20}

#Fungsi untuk irisan
def irisan(set_A, set_B):
    return set_A.intersection(set_B)

#Fungsi untuk beda setangkup
def beda_setangkup(set_A, set_B):
    return set_A.symmetric_difference(set_B)

#Fungsi peluang
def peluang(himpunan, semesta):
    return len(himpunan) / len(semesta)

#Menghitung irisan dan beda setangkup
irisan_himpunan = irisan(A, B)
beda_setangkup_himpunan = beda_setangkup(A,B )

#menghitung peluang P(A) dan P(B)
semesta = A.union(B) # Gabungan himpunan sebagai semesta
peluang_A = peluang(A, semesta)
peluang_B = peluang(B, semesta)

#Ouput hasil
print("Irisan (A n B)"): irisan_himpunan
print("Beda setangkup (A B):",beda_setangkup_himpunan)
print("Peluang P(A):",peluang_A)
print("Peluang P(B):",peluang_B)



#Soal bagian 3, nomor 1. Buat fungsi untuk mengurutkan himpunan A dengan menggunakan buble sort def buble_sort(A):
def bubble_sort(A):
    # Mengubah himpunan menjadi list agar bisa diurutkan
    A = list(A)

    n = len(A)
    for i in range(n):
        # Flag untuk mengecek jika ada perubahan dalam iterasi ini
        swapped = False
        
        # Loop untuk perbandingan elemen yang bersebelahan
        for j in range(0, n-i-1):
            # Jika elemen lebih besar dari elemen berikutnya, tukar
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        
        # Jika tidak ada yang ditukar, berarti sudah terurut
        if not swapped:
            break
    
    return A

#Himpunan A
A = {109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21, 378, 400, 101, 201, 301, 1}

#Mengurutkan himpunan A menggunakan Buble sort
sorted_A = bubble_sort(A)
print(sorted_A)

#Soal bagian 3, nomor 2. Buat fungsi untuk melakukan pencarian nilai x = 300, ada diposisi index ke i
def cari_nilai(A, x):
    #Melakukan pencarian linear
    for i in range(len(A)):
        if A[i] == x:
            # Kembalikan indeks jika ditemukan 
            return i 
        # Kembalikan -1 jika x tidak ditemukan
        return -1
    
# Contoh penggunaan
A = [109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21, 378, 400, 101, 201, 301, 1]
x = 300
index = cari_nilai(A, x)

if index != -1:
    print(f"nilai {x} ditemukan diposisi index ke-{index}.")
else:
    print(f"nilai {x} tidak ditemukan.")
    




    




