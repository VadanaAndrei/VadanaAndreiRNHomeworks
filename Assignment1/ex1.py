import pathlib

def load_system(path: pathlib.Path) -> tuple[list[list[float]], list[float]]:
    A = []
    B = []

    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            left, right = line.split("=")
            right = float(right.strip())

            terms = left.split()

            coeffs = []
            i = 0
            while i < len(terms):
                term = terms[i]
                sign = 1

                if term == '+':
                    sign = 1
                    i += 1
                    term = terms[i]
                elif term == '-':
                    sign = -1
                    i += 1
                    term = terms[i]

                coef = term.replace("x", "").replace("y", "").replace("z", "")
                if coef == '':
                    coef = 1
                coeffs.append(sign * float(coef))
                i += 1

            A.append(coeffs)
            B.append(right)

    return A, B


if __name__ == "__main__":
    path = pathlib.Path("system.txt")
    A, B = load_system(path)
    print(A)
    print(B)