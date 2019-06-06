liste = [3,5,1]
def tri_s(T):
	n=len(T)
	for i in range (n):
		k=i
		for j in range (i+1,n):
			if T[k]>T[j] :
				k=j
		T[k],T[i]=T[i],T[k]
	return T

print(tri_s(liste))