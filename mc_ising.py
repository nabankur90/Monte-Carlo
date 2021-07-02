import numpy as np
import subprocess
import random
import math
from random import randrange

with open("gh1","r")as fh:
	line=fh.read().splitlines()
A=line[1].split()
atom_info=[int(line[0]), float(A[1]), float(A[2]), float(A[3]), float(A[4]), float(A[5]), float(A[6])]
B=np.array([o.split() for o in line[2:atom_info[0]+2]])
elements=B[:,0]
coords=B[:,1:4].astype("float")
Al = [i for i in range(len(elements)) if elements[i]=="Al"]
O = [i for i in range(len(elements)) if elements[i]=="O"]

def file_edit(data,x):
	with open(data,"r") as f_in:
		line=f_in.read().splitlines()
	fout = open("data.txt","w")
	fout.write(format(line[0])+"\n")
	fout.write(format(line[1])+"\n")
	fout.write(format(line[2])+"\n")
	fout.write(format(line[3])+"\n")
	for i in range(4,len(line)):
		if i not in x:
			fout.write(format(line[i])+"\n")
		else:
			pass
	fout.write(format(line[-1])+"\n")
	fout.close()
	return fout

def distance(C,p,q):
	dis=np.linalg.norm(C[p,:]-C[q,:])
	return dis

def randomno(x):
	idx=[]
	f=open("index.txt","a")
	c=0
	while c<x:
		n=random.choice(Al)
		p=0
		if n not in idx:
			for i in O:
				if distance(coords,i,n)<=1.87:
					p=1
					break
			if p==0:
				idx.append(n)
				f.write("%4d" % (n))
				c=c+1
	f.write("\n")
	f.close()
	print (idx)
	return idx

def boltzmann(e1,e2):
	kB=1.381*10e-23
	nmol=6.023*10e23
	T=1000
	beta=kB*nmol*T
	return math.exp(-((e2-e1)*4184)/beta)

	
def min_energy(file):
	x=randomno(67)
	file_edit(file,x)
	subprocess.check_output(["cp","data.txt","geo"],universal_newlines=True)
	subprocess.check_output(["./exe"],universal_newlines=True)
	with open("fort.74","r") as Fh:
		Lines=Fh.read().splitlines()
	A=np.array([o.split() for o in Lines], dtype='object')
	e=float(A[0,2])
	return e	


def MC(n_steps, config):
	subprocess.check_output(["cp","geo1","geo"],universal_newlines=True)
	subprocess.check_output(["./exe"],universal_newlines=True)
	with open("fort.74","r") as fh:
        	Lines=fh.read().splitlines()
	A=np.array([o.split() for o in Lines], dtype='object')
	e_ref = float(A[0,2])
	e_min = e_ref
	eprev = e_ref
	out=open("min_energy.txt","w")
	for i in range(n_steps):
		r=np.random.random()
		ek=min_energy(config)
		if r<boltzmann(e_ref,ek):
			subprocess.check_output(["cp","fort.90","geo"],universal_newlines=True)

			eprev=e_ref
			e_ref=ek
		else:
			pass
		if e_min>ek:
			e_min=ek	
		out.write("%3d %8.4f %8.4f %8.4f \n" % (i, e_ref, eprev, e_min))
	return out

result = MC(100,"geo1")

		
