#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def read(dimensao):
	""" Metodo para ler arquivos das matrizes para serem multiplicadas.
    
    @param dimensao: dimensão das matrizes para serem lidas.

    @return mA: matriz A
    @return mB: matriz B 
    """ 
	matriz_vetor = []
	contador = 0

	matrix_a_path = "../Matrizes/A{0}x{0}.txt".format(dimensao)
	matrix_b_path = "../Matrizes/B{0}x{0}.txt".format(dimensao)

	mA = np.loadtxt(matrix_a_path, skiprows=1)
	mB = np.loadtxt(matrix_b_path, skiprows=1)

	return mA, mB

	
def write(flag, matrix): 
	""" Metodo para escrever em arquivos as matrizes resultantes da multiplicação.
    
    @param matrix: matriz que será gravada no arquivo.
    @param flag: ficará no início do arquivo, para que seja o nome do arquivo e depois a dimensão da matriz gerada

    """ 
	file_name = 'output/{0}/C{1}x{1}.txt'.format(flag, len(matrix)) 
	np.savetxt(file_name, matrix, delimiter=" ", fmt='%-4d')  


if __name__ == '__main__':
	read(2048)


