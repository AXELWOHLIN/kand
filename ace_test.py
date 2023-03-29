import os
import matplotlib.pyplot as plt
import pyne.ace
import requests
import np_csvimport

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
sensitvity_vector = np_csvimport.csv_import(filename)

