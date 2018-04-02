#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import time
import math
import logging
logging.basicConfig(filename='seq.log',level=logging.DEBUG)

from util import read, write
from sequencial import seq_mult
from concorrente3 import conc_mult

import numpy as np

mA, mB = None, None

def variancia(valores, media):
	""" Metodo para efetuar a variância do conjunto de valores passados como argumento.
    
    @param valores: vetor o qual se deseja obter a variância.
    @param media: media dos valores passados por parâmetro

    @return variancia: variância dos valores
    """ 
	soma = 0
	variancia = 0
	for valor in valores:
		soma += math.pow((valor - media), 2)
		variancia = soma/float(len(valores))
	return variancia
 
 
def desvio_padrao(valores, media):
	desvio_padrao = math.sqrt(variancia(valores, media))
	return desvio_padrao

def main(argv):
	global mA, mB
	""" Metodo main que executa a ação principal de multiplicar as duas matrizes, a partir da flag dada na linha de comando iremos usar um método diferente para multiplicar.
    
    @param argv: flags que direcionam o calculo da multiplicação (se será sequencial, concorrrente ou o experimento.

    """  
	parser = argparse.ArgumentParser(description='Realiza a multiplicação de duas matrizes quadradas.')
	parser.add_argument('--dimensao', 
						metavar='N', 
						type=int,  
	                   	help='Número inteiro que representa a dimensão das matrizes quadradas que serão tratadas pelo programa. Valores deverão ser de potências de base 2.')
	parser.add_argument('--algoritmo',
						metavar='S|C',   
	                    help='Os caracteres S e C indicam respectivamente que será utilizada a solução sequencial ou a solução concorrente.') 
	parser.add_argument('--experimento',
						metavar='N',    
	                    help='Flag para realizar o experimento com todas as matrizes.') 

	args = parser.parse_args() 
	
	if args.experimento:
		d = 2
		time_total = 0
		valores = []

		mAs = []
		mBs = []

		logging.info(" ----- SEQ ----- ")

		for e in range(10):
			time_max = -1
			time_min = -1

			d = d * 2
			mA, mB = read(d) 
			mAs.append(mA)
			mBs.append(mB)

			for i in range(int(args.experimento)): 
				start_time = time.clock()
				seq_mult(mA, mB)
				time_inst = time.clock() - start_time

				if (time_inst <= time_min or time_min == -1):
					time_min = time_inst
				if (time_inst >= time_max):
					time_max = time_inst
				
				time_total += time_inst
				valores.append(time_inst)

			time_m = time_total/20
			logging.info("A média de execução é de: " + str(time_m) + "s na matriz de ordem "+ str(d))
			logging.info("Maior tempo de execução foi: "+str(time_max) + "s")
			logging.info("Menor tempo de execução foi: "+str(time_min) + "s")
			logging.info("O desvio padrão é de: " + str(desvio_padrao(valores,time_m)) + "s")


		logging.info(" ----- CONC ----- ")

		d = 2
		for e in range(10):
			time_max = -1
			time_min = -1

			d = d * 2

			for i in range(int(args.experimento)): 
				print(e, i)
				start_time = time.clock()
				conc_mult(mAs[e], mBs[e])
				time_inst = time.clock() - start_time

				if (time_inst <= time_min or time_min == -1):
					time_min = time_inst
				if (time_inst >= time_max):
					time_max = time_inst

				time_total += time_inst
				valores.append(time_inst)

			time_m = time_total/20
			logging.info("A média de execução é de: " + str(time_m) + "s na matriz de ordem "+ str(d))
			logging.info("Maior tempo de execução foi: "+str(time_max) + "s")
			logging.info("Menor tempo de execução foi: "+str(time_min) + "s")
			logging.info("O desvio padrão é de: " + str(desvio_padrao(valores,time_m)) + "s")

	else:
		error = []
		if args.dimensao % 2 != 0 or args.dimensao < 4 or args.dimensao > 2048:
			error.append("ERROR: valor %s inválido para dimensão" % args.dimensao)
			 
		if not args.dimensao:
			error.append("ERROR: é necessário valor para dimensão")
			 
		if not args.algoritmo:
			error.append("ERROR: é necessário identificar o algoritmo") 

		if error: 
			for e in error: print(e)
			sys.exit(1)

		mA, mB = read(args.dimensao) 

		if args.algoritmo == 'S':
			start_time = time.clock()
			m = seq_mult(mA, mB)
			time_inst = time.clock() - start_time
			print("time execution %s" % str(time_inst))
			write('S', m)
		elif args.algoritmo == 'C': 
			start_time = time.clock()
			m = conc_mult(mA, mB)
			time_inst = time.clock() - start_time
			print("time execution %s" % str(time_inst))
			write('C', m)

if __name__ == "__main__":
   main(sys.argv[1:])
