import numpy
import random
import string
import os
from string import *
from random import *
#from os import *

# функция, генерирующая текстовые файлы заданного размера
def generate():
	# генерируем по 10 файлов размера от 10 байт до 10^7 байт
	# не претендуем на статистическую полноту
	# поэтому в демонстрационных целях можно ограничиться десятью файлами каждого размера
	for i in range(1, 8):
		for j in range(1, 11):
			res = ''
			with open('file_{}_{}.txt'.format(i, j), "w") as f:
				res = ''.join(choice(string.printable) for n in range(10**i))
				f.write(res)
				print("file_{}_{}.txt created".format(i, j))


if __name__ == "__main__":

	old_dir = os.getcwd()
	working_dir = old_dir + "/files"
	
	if not os.path.exists(working_dir):
		res = os.makedirs(working_dir)
	os.chdir(working_dir) # переходим в папку files в текущей рабочей директории
	
	generate() # ссуществляем генерацию тестовых файлов для проверки архивации
	os.chdir(old_dir) # возвращаемся в исходную директорию
