from constraint import *

columns = []
rows = []
with open("kakuro_input.txt", "r") as kakuro_input:
    counter = 0
    for line in kakuro_input:
        if counter == 0:
            columns = line.strip().replace(" ", "").split(",")
        if counter == 1:
            rows = line.strip().replace(" ", "").split(",")
        counter += 1

zToN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = ["a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"]
problem = Problem()
problem.addVariable(l[0], zToN)
problem.addVariable("a2", zToN)
problem.addVariable("a3", zToN)
problem.addVariable("b1", zToN)
problem.addVariable("b2", zToN)
problem.addVariable("b3", zToN)
problem.addVariable("c1", zToN)
problem.addVariable("c2", zToN)
problem.addVariable("c3", zToN)
problem.addConstraint(lambda a1, a2, a3, b1, b2, b3, c1, c2, c3: (a1 != a2 and a2 != a3) and (b1 != b2 and b2 != b3) and
                                                                 (c1 != c2 and c2 != c3) and (a1 != b1 and b1 != c1) and
                                                                 (a2 != b2 and b2 != c2) and (a3 != b3 and b3 != c3),
                      ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"))

problem.addConstraint(lambda a1, a2, a3: a1 + a2 + a3 == int(columns[0]), ("a1", "a2", "a3"))
problem.addConstraint(lambda b1, b2, b3: b1 + b2 + b3 == int(columns[1]), ("b1", "b2", "b3"))
problem.addConstraint(lambda c1, c2, c3: c1 + c2 + c3 == int(columns[2]), ("c1", "c2", "c3"))
problem.addConstraint(lambda a1, b1, c1: a1 + b1 + c1 == int(rows[0]), ("a1", "b1", "c1"))
problem.addConstraint(lambda a2, b2, c2: a2 + b2 + c2 == int(rows[1]), ("a2", "b2", "c2"))
problem.addConstraint(lambda a3, b3, c3: a3 + b3 + c3 == int(rows[2]), ("a3", "b3", "c3"))

solution = problem.getSolution()

with open("kakuro_output.txt", "w") as kakuro_output:
    kakuro_output.write("X, " + ", ".join(columns) + "\n")
    rep = 0
    row = 0
    for k in l:
        rep += 1
        if rep == 1:
            kakuro_output.write(rows[row] + ", ")
            row += 1
        if rep == 3:
            kakuro_output.write(str(solution[k]) + "\n")
            rep = 0
        else:
            kakuro_output.write(str(solution[k]) + ", ")
