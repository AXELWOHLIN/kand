import os
import matplotlib.pyplot as plt
import pyne.ace
import requests
import np_csvimport
import numpy as np

url = "https://www-nds.iaea.org/wolfram/w180/beta3/W180.ace"
r = requests.get(url)
with open("W180.ace", "wb") as outfile:
    outfile.write(r.content)

lib = pyne.ace.Library('W180.ace')
lib.read('74180.21c')
lib.tables
w180 = lib.tables['74180.21c']
total_xs = w180.sigma_t
energy = w180.energy

filename = 'csv_files/totalgodiva-Sheet1.csv'
sens_vector_energy, sens_vector_values = np_csvimport.csv_import(filename)

energy *= 1e+06
print(f"Energy xs shape is {np.shape(energy)}") #2600, 1e-11 till 5e+01
print(f"Sens vec energy shape is {np.shape(sens_vector_energy)}") # 239, 1e-05 20000000.0


plt.figure()
plt.loglog(energy,total_xs)


plt.figure(2)
plt.loglog(sens_vector_energy,sens_vector_values)
plt.show()
