def mirror_matrix(matrix):
    return matrix[::-1] 
matrix=[[1,2,3],[4,5,6],[7,8,9]] #output:[[7,8,9],[4,5,6],[1,2,3]]
print(mirror_matrix(matrix))
def rotate_image(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()
    return matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]] #output:[[7,4,1],[8,5,2],[9,6,3]]
print(rotate_image(matrix))