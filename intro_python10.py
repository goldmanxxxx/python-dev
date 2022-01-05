import csv

# tentukan lokasi file, nama file, dan inisialisasi csv
f = open('dkikepadatankelurahan2013.csv', 'r')
reader = csv.reader(f)

# membaca baris per baris
for row in reader:
	print (row)

# menutup file csv
f.close()