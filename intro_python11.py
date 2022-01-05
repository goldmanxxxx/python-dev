import matplotlib.pyplot as plt 
import csv

plt.style.use('ggplot')

x=[]
y=[]

with open('penduduk_gender.csv','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(row[5]+row[6])
        
label=row[4]

x_pos = [i for i, _ in enumerate(label)]
plt.bar(label,x)
plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x_pos, label)

plt.show()