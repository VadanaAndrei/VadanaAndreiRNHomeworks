from ex3 import *

def minor(matrix: list[list[float]], i: int, j: int) -> list[list[float]]:
    return [ [matrix[r][c] for c in range(len(matrix)) if c != j]
             for r in range(len(matrix)) if r != i]

def cofactor(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            m = minor(matrix, i, j)
            row.append(((-1) ** (i + j)) * determinant(m))
        cof.append(row)
    return cof

def adjoint(matrix: list[list[float]]) -> list[list[float]]:
    cof = cofactor(matrix)
    n = len(cof)
    return [[cof[j][i] for j in range(n)] for i in range(n)]

def solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    det_A = determinant(matrix)
    if det_A == 0:
        raise ValueError("The system does not have a unique solution.")

    A_inv = [[adjoint(matrix)[i][j] / det_A for j in range(3)] for i in range(3)]
    return multiply(A_inv, vector)

if __name__ == "__main__":
    path = pathlib.Path("system.txt")
    A, B = load_system(path)
    solution = solve(A, B)
    print(f"solve(A, B) = {solution}")