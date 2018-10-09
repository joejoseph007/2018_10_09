
import random, re,  subprocess, sys, os, math ,numpy,shutil
import matplotlib.pyplot as plt
import stl
from stl import mesh
from distutils.dir_util import copy_tree
from multiprocessing import Pool
import scipy.interpolate as si

def read_integers(filename,t):
    with open(filename) as f:
        if t=='f':
            return [float(x) for x in f]
        
        if t=='i':
            z=[int(x) for x in f]
            return z[0]

        if t=='fxy':
            x=[];y=[]
            for i in f:
                row = i.split()
                x.append(float(row[0]))
                y.append(float(row[1]))

            return x,y



X,Y=read_integers('Points', "fxy")


#print(X,Y)

density=2.7e-3#g/mm^3
width=20#mm
thickness=0.1#mm



sum1=0
for i in range(len(X)):
    R=((X[i])**2+(Y[i])**2)**0.5
    sum1=sum1+R

length=[]
X1=[]
Y1=[]
for i in range(len(X)-1):
    length.append((((X[i]-X[i+1]))**2+((Y[i]-Y[i+1]))**2)**0.5)
    X1.append((X[i]+X[i+1])/2)
    Y1.append((Y[i]+Y[i+1])/2)

Mass=[(length[i]*thickness*width*density) for i in range(len(length))]
Moi=[Mass[i]*((X1[i])**2+(Y1[i])**2) for i in range(len(length)) ]
print(3*sum(Moi)/(1e+9),'Kgm^2',3*sum(Mass)/(1e+3),'Kg')

#print(sum1,length,len(X))

thefile = open('Jlength', 'w')

thefile.write("%.6f %.6f %i" %(3*sum(Moi),3*sum(Mass),len(X)))#randf(random.randrange(random.randrange(-150,-145),-70),0))
thefile.close()
