import random

character = "abcdefghijklmnopqrstuvwxyz" #! Memasukkan karakter yang akan di bruteForce ke dalam Variabel
charddata = list(character) 
"""Mengubah isi dari variabel "character" menjadi sebuah list yang apabila kita print akan 
   menghasilkan output:
   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z']"""


password = str(input("Masukkan Password kamu: ")) #! meminta user untuk memasukkan Password
myGuess = "" #! membuat variabel kosong, yang nantinya akan digunakan untuk memecah Password (Konsepnya karena myGuess kosong jadinya myGuess != dengan "password" yang isinya sudah diisi oleh user)

while (myGuess != password): #? taulah, udah gw jelasin di atas (pokoknya myGuess gak sama ama password karena myGuess kosong sedangkan password nilainya sudah diisi oleh kita)
    myGuess = random.choices(charddata, k=len(password)) #todo: chardData:  Ini adalah list dari karakter yang akan digunakan sebagai sumber untuk pemilihan acak, dan k itu kek panjang dari isi password. misal user input 6 kata maka program akan membobol 6 kata
    print(myGuess) #? Mencetak hasil dari password yang telah di ketahui di myGuess
    myGuess="".join(myGuess) #! digunakan untuk menyatukan list yang terpisah misal = ["B", "A", "B"], yang awalnya terpisah akan tercetak jadi = BAB
print(f"Password kamu adalah: {myGuess}")

