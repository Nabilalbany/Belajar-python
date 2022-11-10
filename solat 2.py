#Soal 1: Apa perbedaan dari list, tuple, set, dan dictionary! 

listt = ['nabil', 'ganteng', 'anak pak yams']
tuplee = ('nabil', 'ganteng', 'banget')
sett = {'a', 'b', 'c',}
dictionaryy = {"nama": "babayo", "nama orang tua": "oyaoyapoh",}

#Soal 2: Akses list

a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print (a[1:5])

#SOAL 3: Nested list

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
print (a[1][1:])

#SOAL 4: List Manipulation

a = [
    [5, 9, 8],
    [0, 0, 6]
    ] 
    
a[0][2] = 10
a[1][0] = 11
print (a)

#Soal 5: Delete Element List

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

  
areas.pop(8)
areas.pop(9)
print (areas)

#Soal 6: List Comprehension

S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
T = S[0::2]
print(T)

#Soal 8: Menambahkan key-value baru ke Dictionary

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe.update({"itali":"roma"})

#Soal 9: Boolean Comparison

#Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'and'
#Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'or'
#Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'not'

print((1 > 8) and (1 < 4))	
print((8 == 9) or (6 != 6))	
print(not(1 <= 3))


#Soal 10: If-Else Statement
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

A = 1000000
if A >= 100000:
    print("High")
elif A >= 50000:
    print("Medium")
elif A <= 50000:
    print("Low")

