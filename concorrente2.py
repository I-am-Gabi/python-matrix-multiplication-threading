#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import threading 
from threading import Lock
lock = Lock()
import time, numpy
  
matrix_c = None   
layers = []

def sum_matrices():     
    global matrix_c, layers 
    for i in range(0, len(matrix_c)):
        for j in range(0, len(matrix_c)):
            for l in layers:
                matrix_c[i][j] += l[i][j]

class ThreadMatrix(threading.Thread):
    """ 
        Metodo para criar e matar as threads que serão usadas no cálculo da 
        multiplicação de matrizes e representarão cada linha da matriz final.
    """ 
    def __init__(self, id, size, vector_a, vector_b):
        threading.Thread.__init__(self)
        self.id = id
        self.size = int(size) 
        self.vector_a = vector_a
        self.vector_b = vector_b

    def run(self):   
        matrix_c_aux = numpy.zeros(shape=(self.size, self.size)) 
        for i in range(0, self.size):
            for j in range(0, self.size):
                sum_ = self.vector_a[i] * self.vector_b[j]    
                matrix_c_aux[i][j] += sum_ 
        layers.append(matrix_c_aux) 

def conc_mult(matrix_A, matrix_B):
    """ Metodo para efetuar a multiplicação entre duas matrizes de forma concorrente.
    
    @param matrix_A: matriz A que será multiplicada pela B.
    @param matrix_B: matriz B que será multiplicada pela A.

    @return matrix_c: matriz resultante da multiplicação dos dois parâmetros de entrada
    """ 
    global matrix_c
    size = len(matrix_A) 

    matrix_c = numpy.zeros(shape=(size,size))  

    threads = []
    for thread_id in range(size):
        t = ThreadMatrix(thread_id, size, matrix_A[:,[thread_id]], matrix_B[thread_id])
        threads.append(t)
        t.start() 

    for t in threads: t.join()
 
    sum_matrices() 
    return matrix_c
