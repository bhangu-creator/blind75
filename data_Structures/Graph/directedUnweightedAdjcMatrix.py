class directed_Graph:
    def add_edge(self,mat,i,j):
        mat[i][j]=1
    def show_matrix(self,mat):
        for row in mat:
            print(''.join(map(str,row)))
    def create_matrix(self,n):
        mat=[[0 for _ in range(n)] for _ in range(n)]
        return mat
    
sol=directed_Graph()
mat=sol.create_matrix(4)
sol.add_edge(mat,0,1)
sol.add_edge(mat,0,2)
sol.add_edge(mat,1,2)
sol.add_edge(mat,2,3)
sol.show_matrix(mat)

