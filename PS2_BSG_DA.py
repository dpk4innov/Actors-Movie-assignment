class BSGraph:
	
	def __init__(self,inp):
		self.input=inp
		inputfile=self.input
		self.m=[]
		self.a=[]
		self.edge=[[]]
	def readActMovfile(self, inputfile):
		fp=open(inputfile,"r")
		for i in fp:
			str1=(i.rstrip()).split('/')
			(self.m).append(str1[0])
			if str1[1] not in self.a:
				self.a.append(str1[1])
			if len(str1)>2 and str1[2] not in self.a:
				self.a.append(str1[2])
		print(self.a)
		print(self.m)
		fp.close()
		fo=open(inputfile,"r")
		self.edge=[[0]*len(self.a) for x in range(0,len(self.m))]
		k=0
		for i in fo:
	
			str1=(i.rstrip()).split('/')
			j=self.a.index(str1[1])
			self.edge[k][j]=1
			if len(str1)>2:
				j=self.a.index(str1[2])
				self.edge[k][j]=1
			k=k+1
		for i in self.edge:
			print(i)
	def displayActMov(self):
		fp=open("outputPS2.txt","w")
		fp.write("--------Function displayActMov--------\n") 
		fp.write("Total no. of movies:%d\n"%(len(self.m)))
		fp.write("Total no. of actors:%d\n"%(len(self.a)))
		fp.write("List of movies:\n")
		for i in range(0,len(self.m)):
			fp.write(self.m[i])
			fp.write("\n")
		fp.write("List of actors:\n")
		for i in range(0,len(self.a)):
			fp.write(self.a[i])
			fp.write("\n")
		fp.write("-----------------------------------\n") 
		
	def displayMoviesOfActor(self):
		fo=open("promptsPS2.txt","r")
		fp=open("outputPS2.txt","a")
		fp.write("--------Function displayMoviesOfActor--------\n") 
		for i in fo:
			str1=(i.rstrip()).split(':')
			
			if str1[0]=="searchActor":
				if str1[1] not in self.a:
					fp.write("Actor not found")
					fp.write("\n")
				j=self.a.index(str1[1])
				fp.write("Actor name:")
				fp.write(str1[1])
				fp.write("\n")
				fp.write("List of Movies:\n")
				for k in range(0,len(self.m)):
					if self.edge[k][j]==1:
						fp.write(self.m[k])
						fp.write("\n")
		fp.write("-----------------------------------\n") 
		
					

	def displayActorsOfMovie(self):
		fo=open("promptsPS2.txt","r")
		fp=open("outputPS2.txt","a")
		fp.write("--------Function displayActorsOfMovie--------\n")
		for i in fo:
			str1=(i.rstrip()).split(':')
			
			if str1[0]=="searchMovie":
				if str1[1] not in self.m:
					fp.write("Movie not found")
					fp.write("\n")
				j=self.m.index(str1[1])
				fp.write("Movie name:")
				fp.write(str1[1])
				fp.write("\n")
				fp.write("List of Actors:\n")
				for k in range(0,len(self.a)):
					if self.edge[j][k]==1:
						fp.write(self.a[k])
						fp.write("\n")
		fp.write("-----------------------------------\n") 
		
					

	def findMovieRelation(self):
		fo=open("promptsPS2.txt","r")
		fp=open("outputPS2.txt","a")
		fp.write("--------Function findMovieRelation--------\n")
		for i in fo:
			str1=(i.rstrip()).split(':')
			if str1[0]=="RMovies":
				j=self.m.index(str1[1])
				j1=self.m.index(str1[2])
				fp.write("Movie A:")
				fp.write(str1[1])
				fp.write("\n")
				fp.write("Movie B:")
				fp.write(str1[2])
				fp.write("\n")
				a=-1
				for k in range(0,len(self.a)):
					if self.edge[j][k]==1 and self.edge[j1][k]==1:
						a=k
						fp.write("Related: Yes,")						
						fp.write(self.a[k])
						fp.write("\n")
					
				if a==-1:
					fp.write("Related: No")
					fp.write("\n")
		fp.write("-----------------------------------\n")	
	def findMovieTransRelation(self):
		fo=open("promptsPS2.txt","r")
		fp=open("outputPS2.txt","a")
		fp.write("--------Function findMovieTransRelation--------\n")
		for i in fo:
			str1=(i.rstrip()).split(':')
			if str1[0]=="TMovies":
				j=self.m.index(str1[1])
				j1=self.m.index(str1[2])
				fp.write("Movie A:")
				fp.write(str1[1])
				fp.write("\n")
				fp.write("Movie B:")
				fp.write(str1[2])
				fp.write("\n")
				d=-1
				for k in range(0,len(self.a)):
					if self.edge[j][k]==1:
						b=k
						for x in range(0,len(self.m)):
							if self.edge[x][b]==1:
								a=b					
								c=x
								for k in range(0,len(self.a)):
									if self.edge[c][k]==1 and self.edge[j1][k]==1:
										d=c
										fp.write("Related: Yes,")	
										fp.write(str1[1]+'>'+self.a[a]+'>'+self.m[d]+'>'+self.a[k]+'>'+str1[2]+'\n')

				if d==-1:
					fp.write("Related: No\n")
		fp.write("-----------------------------------\n")	
g=BSGraph("inputPS2.txt")
g.readActMovfile("inputPS2.txt")
g.displayActMov()
g.displayMoviesOfActor()
g.displayActorsOfMovie()
g.findMovieRelation()		
g.findMovieTransRelation()			
