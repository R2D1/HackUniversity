import numpy
import random
import string
import os
from string import *
from random import *
#from os import *

# функция, генерирующая текстовые файлы размера 10^n байт
def generate():
	# генерируем по 50 файлов размера от 10 байт до 10^7 байт
	for i in range(1, 8):
		for j in range(1, 51):
			res = ''
			file_name = 'file_{}_{}.txt'.format(i, j)
			with open(file_name, "w") as f:
			
				res = ''.join(choice(string.printable) for n in range(10**i))
				f.write(res)
				print("File_{}_{}.txt created".format(i, j))


if __name__ == "__main__":

	old_dir = os.getcwd()
	working_dir = old_dir + "/files"

	if not os.path.exists(working_dir):
		res = os.makedirs(working_dir)
	os.chdir(working_dir)
	generate()
	os.chdir(old_dir)
