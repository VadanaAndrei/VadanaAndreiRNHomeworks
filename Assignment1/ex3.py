from ex2 import *

def solve_cramer(matrix: list[list[float]], vector: list[float]) -> list[float]:
    det_A = determinant(matrix)
    if det_A == 0:
        raise ValueError("The system does not have a unique solution.")

    solutions = []
    for col in range(3):
        temp = [row.copy() for row in matrix]
        for i in range(3):
            temp[i][col] = vector[i]
        solutions.append(determinant(temp) / det_A)

    return solutions

if __name__ == "__main__":
    path = pathlib.Path("system.txt")
    A, B = load_system(path)
    cramer_sol = solve_cramer(A, B)
    print(f"solve_cramer(A, B) = {cramer_sol}")