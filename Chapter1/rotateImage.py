def rotate_image(matrix):
  rows = len(matrix)
  cols = len(matrix[0])

  #Transpose a matrix
  for i in range(rows):
    for j in range(i+1,cols):
      matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]  
  #reverse each row.   
  for row in range(rows):
    matrix[row].reverse()
  print(matrix)


print(rotate_image([[1, 2, 3], [4, 5, 6],[7,8,9]]))