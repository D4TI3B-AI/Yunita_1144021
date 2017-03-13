import time
start_time = time.time()

angka = {
        'satu' : 1, 'dua' : 2, 'tiga' : 3, 'empat' : 4, 'lima' : 5, 'enam' : 6, 'tujuh' :7, 'delapan' : 8, 'sembilan' : 9}

print("Menghitung (a + b)+(c - d)")
a = raw_input ('nilai a : ')
b = raw_input ('nilai b : ')
c = raw_input ('nilai c : ')
d = raw_input ('nilai d : ')

if a in angka :
    a = angka[a]

if b in angka :
    b = angka[b]

if c in angka :
    c = angka[c]

if d in angka :
    d = angka[d]

hasil = (a + b) + (c - d)

print("Waktu Eksekusi : %s detik " % (time.time() - start_time))
