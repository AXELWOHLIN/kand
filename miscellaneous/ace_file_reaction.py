import os
import matplotlib.pyplot as plt
import pyne.ace
from pyne.xs import models
import pyne.rxname as rx
import requests
import numpy as np
from pyne.rxname import *
from tkinter import Tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from scipy.stats import skew
from scipy.stats import norm, kurtosis
from pyne.xs import models




ace_file = 'ACE_files/Pu239.nuss.05.10.2016/Pu239-n.ace_0000'
directory = 'ACE_files/Pu239.nuss.05.10.2016'

with open(ace_file, 'rb') as infile:
    ace_file_contents = infile.read()

# Write the contents to a new file
with open('new_file.ace', 'wb') as outfile:
    outfile.write(ace_file_contents)
lib = pyne.ace.Library('new_file.ace')
for entry in os.scandir(directory):
        if entry.is_file() and ".xsdir" in entry.name:
            dir_file = entry.path
            break
with open(dir_file) as f:
    first_line = f.readline()
    first_word = first_line.split()[0]
lib.read(first_word)
lib.tables

file_contents = lib.tables[first_word]



energy = file_contents.energy
xs_chi = models.chi(energy)

chi = file_contents.xs['chi'] 

reaction = file_contents.reactions

for key, value in reaction.items():
    mt_number = key
    print(rx.label(int(mt_number)))

if os.path.exists('new_file.ace'):
    os.remove('new_file.ace')
