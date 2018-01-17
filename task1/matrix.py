TestMatrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]

def trans_matrix(matrix):
	"""trans_matrix(matrix) -- transpose  matrix"""

	matrix[:] = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def del_column(matrix, num):
	"""del_column(matrix) -- delete column with num item"""

	trans_matrix(matrix)
	for i in range(len(matrix)):
		if num in matrix[i]:
			del matrix[i]
			break
	trans_matrix(matrix)
