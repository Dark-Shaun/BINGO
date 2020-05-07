import numpy
import np
from random import randint
from name import *
from define import *
name_1,name_2=pname()
print("----------------------------------------------------------------------------")
A_1,B_1,A,B=define()

print("Fill the matrix by values from 1 to 30 numbers randomly:")
print("----------------------------------------------------------------------------")
A=entries1()
print("----------------------------------------------------------------------------")
print("{}:{}".format(A,name_1))
print("----------------------------------------------------------------------------")
B=entries2()
print("----------------------------------------------------------------------------")
print("{}:{}".format(B,name_2))


k=[]

while len(k)!=30:
    m=randint(1,30)
    if m not in k:
        k.append(m)
print("----------------------------------------------------------------------------")
for l in range(0,30):
    y=int(input("Enter 1 to draw next number:"))
    if y==1:
        print("The Number is:{}".format(k[l]))
        if k[l] in A:
            a=list(zip(np.where(A==k[l])))
            r=list(zip(a[0], a[1]))
            x,y=r[0]
            A[x[0]][y[0]]=0
        
        print("{}:{}".format(A,name_1))
        print('----------------------')
        if k[l] in B:
            a=list(zip(np.where(B==k[l])))
            r=list(zip(a[0], a[1]))
            x,y=r[0]
            B[x[0]][y[0]]=0
        
        print("{}:{}".format(B,name_2))
        print('----------------------')
    
    
        h=A_1==A
        s=B_1==B
        if h.all() or s.all():
            if h.all()==True:
                print('BINGO\n{} WINS!!!!!'.format(name_1))
            else:
                print('BINGO\n{} WINS!!!!!'.format(name_2))
            break
    else:
        print("Wrong Number")

print("--------------------------------------------------------------------------------------------------------------------")
print("GAME OVER")
 

        

    
    

    
    
