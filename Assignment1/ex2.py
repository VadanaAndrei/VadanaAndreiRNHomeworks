from ex1 import *
import math

def determinant(matrix: list[list[float]]) -> float:
    n = len(matrix)
    if n == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return a * d - b * c
    elif n == 3:
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def trace(matrix: list[list[float]]) -> float:
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))

def norm(vector: list[float]) -> float:
    return math.sqrt(sum(x**2 for x in vector))

def transpose(matrix: list[list[float]]) -> list[list[float]]:
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

def multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = []
    for row in matrix:
        s = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(s)
    return result


if __name__ == "__main__":
    path = pathlib.Path("system.txt")
    A, B = load_system(path)
    det = determinant(A)
    tr = trace(A)
    nrm = norm(B)
    A_T = transpose(A)
    res = multiply(A, B)
    print(f"determinant(A) = {det}")
    print(f"trace(A) = {tr}")
    print(f"norm(B) = {nrm}")
    print(f"transpose(A) = {A_T}")
    print(f"multiply(A, B) = {res}")