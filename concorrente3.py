#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import threading 
from threading import Lock, Thread 
lock = Lock()
import time, numpy
  
matrix_c = None     

def run(size, vector_a, vector_b):   
    for i in range(0, size):
        for j in range(0, size):
            sum_ = vector_a[i] * vector_b[j]    
            #lock.acquire()
            matrix_c[i][j] += sum_
            b.wait()
            #lock.release() 

def conc_mult(matrix_A, matrix_B):
    """ Metodo para efetuar a multiplicação entre duas matrizes de forma concorrente.
    
    @param matrix_A: matriz A que será multiplicada pela B.
    @param matrix_B: matriz B que será multiplicada pela A.

    @return matrix_c: matriz resultante da multiplicação dos dois parâmetros de entrada
    """ 
    global matrix_c
    size = len(matrix_A) 
    #b = Barrier(size)
    matrix_c = numpy.zeros(shape=(size,size))  

    threads = []
    for thread_id in range(size):
        threads.append(Thread(target=run(size, matrix_A[:,[thread_id]], matrix_B[thread_id])))
        t.start() 

    for t in threads: t.join()

    return matrix_c
