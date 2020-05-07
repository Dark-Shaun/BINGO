import numpy
import np
from random import randint
def define():
	A_1=np.zeros((3,3),dtype=int)
	B_1=np.zeros((3,3),dtype=int)
	A=np.zeros((3,3),dtype=int)
	B=np.zeros((3,3),dtype=int)
	return A_1,B_1,A,B

def entries1():
	A=np.zeros((3,3),dtype=int)
	for i in range(0,3):
		for j in range(0,3):
			k=input("Entries:")
			A[i][j]=k
	return A

def entries2():
	B=np.zeros((3,3),dtype=int)
	for i in range(0,3):
		for j in range(0,3):
			k=input("Entries:")
			B[i][j]=k
	return B