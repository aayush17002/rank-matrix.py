#Aayush Gupta 2017002

#To swap the rows
def swapRows(A,row1,row2):
	x=A[row1]
	A[row1]=A[row2]
	A[row2]=x

#for transformation of rows
def Row_Transformation(A,x,row1,row2):
	l=len(A[0])
	for i in range(l):
		A[row2][i]=A[row2][i]-x*A[row1][i]

#To obtain the RREF matrix of the given matrix
def RREFMatrix(A):
	if not A:
		return
	leading=0
	Nrows=len(A)
	Ncols=len(A[0])
	for t in range(Nrows):
		if leading>=Ncols:
			return
		x=t
		while A[x][leading]==0:
			x+=1
			if x==Nrows:
				x=t
				leading+=1
				if Ncols==leading:
					return
		swapRows(A,x,t)
		r=A[t][leading]
		A[t]=[a/float(r) for a in A[t]]
		for x in range(Nrows):
			if x!=t:
				r=A[x][leading]
				Row_Transformation(A,r,t,x)
		leading+=1

#to obtain the rank from RREF matrix
def MatrixRank(A):
	rank=0
	for t in range(len(A)):
		for i in range(len(A[0])):
			if A[t][i]==1 and i>=t:
				rank+=1
				t=i
				break
	return rank

if __name__=="__main__":
	# matrix=eval(input("enter a matrix: "))
	matrix=[[0,0,0],[0,4,0],[0,0,0]]
	RREFMatrix(matrix)
	# for row in matrix:
	#   print (', '.join( (str(col) for col in row) ))
	print(MatrixRank(matrix))