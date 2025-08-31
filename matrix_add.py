from array import array

def input_matrix(rows, cols):
    mat = []
    for i in range(rows):
        row = array("i", [])
        for j in range(cols):
           row.append(int(input(f"Enter element ({i}, {j}): ")))
        mat.append(row)

    return mat

def add_matrix(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Unable to add matrices with different shape!")
        return None

    m3 = []
    for i in range(len(m1)):
        row = array("i", [])
        for j in range(len(m2)):
            row.append(m1[i][j] + m2[i][j])
        m3.append(row)

    return m3

def display_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


r1, c1 = list(map(int, input("Enter rows & cols of matrix 1: ").split()))
mat1 = input_matrix(r1, c1)

r2, c2 = list(map(int, input("Enter rows & cols of matrix 2: ").split()))
mat2 = input_matrix(r2, c2)

print("\nResult of addition:")
display_matrix(add_matrix(mat1, mat2))
