class directed_Graph:
    def add_edge(self,mat,i,j,w):
        mat[i][j]=w
    def show_matrix(self,mat):
        for row in mat:
            print(' '.join(map(str,row)))
    def create_matrix(self,n):
        mat=[[0 for _ in range(n)] for _ in range(n)]
        return mat
    
sol=directed_Graph()
mat=sol.create_matrix(4)
sol.add_edge(mat,0,1,4)
sol.add_edge(mat,0,2,5)
sol.add_edge(mat,1,2,6)
sol.add_edge(mat,2,3,7)
sol.show_matrix(mat)

