#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

def seq_mult(matrix_A, matrix_B): 
	""" Metodo para efetuar a multiplicação entre duas matrizes de forma sequencial.
    
    @param matrix_A: matriz A que será multiplicada pela B.
    @param matrix_B: matriz B que será multiplicada pela A.

    @return matrix_c: matriz resultante da multiplicação dos dois parâmetros de entrada
    """ 
	size = len(matrix_A)  
	matrix_C = numpy.zeros(shape=(size,size)) 
	
	for i in range(0, size):
		for j in range(0, size):
			soma = 0
			for k in range(0, size):  
				soma += matrix_A.item((i, k)) * matrix_B.item((k, j)) 
			matrix_C.itemset((i, j), soma)
	return matrix_C