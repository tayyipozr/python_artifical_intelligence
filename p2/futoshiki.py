from constraint import *

oToF = [1, 2, 3, 4]
l = ["a1", "b1", "c1", "d1", "a2", "b2", "c2", "d2", "a3", "b3", "c3", "d3", "a4", "b4", "c4", "d4"]
constraints_num = {}
constraints_str = {}
with open("futoshiki_input.txt") as input_file:
    for line in input_file:
        line = line.strip().replace(" ", "").split(",")
        if len(line[1]) == 1:
            constraints_num[line[0].lower()] = line[1]
        else:
            constraints_str[line[0].lower()] = line[1].lower()

problem = Problem()
problem.addVariables(l, oToF)

problem.addConstraint(AllDifferentConstraint(), ("a1", "a2", "a3", "a4"))
problem.addConstraint(AllDifferentConstraint(), ("b1", "b2", "b3", "b4"))
problem.addConstraint(AllDifferentConstraint(), ("c1", "c2", "c3", "c4"))
problem.addConstraint(AllDifferentConstraint(), ("d1", "d2", "d3", "d4"))
problem.addConstraint(AllDifferentConstraint(), ("a1", "b1", "c1", "d1"))
problem.addConstraint(AllDifferentConstraint(), ("a2", "b2", "c2", "d2"))
problem.addConstraint(AllDifferentConstraint(), ("a3", "b3", "c3", "d3"))
problem.addConstraint(AllDifferentConstraint(), ("a4", "b4", "c4", "d4"))
for k in constraints_str:
    problem.addConstraint(lambda a, b: a > b, (k, constraints_str[k]))

for k in constraints_num:
    var = k
    value = constraints_num[k]
    problem.addConstraint(lambda a: str(a) == value, [k, ])

solution = problem.getSolution()
print(solution)
with open("futoshiki_output.txt", "w") as futoshiki_output:
    rep = 0
    for k in l:
        if rep >= 0 and rep < 3:
            futoshiki_output.write(str(solution[k]) + ", ")
        if rep == 3:
            futoshiki_output.write(str(solution[k]))
        if rep == 4:
            futoshiki_output.write("\n")
        if rep >= 4 and rep < 7:
            futoshiki_output.write(str(solution[k]) + ", ")
        if rep == 7:
            futoshiki_output.write(str(solution[k]))
        if rep == 8:
            futoshiki_output.write("\n")
        if rep >= 8 and rep < 11:
            futoshiki_output.write(str(solution[k]) + ", ")
        if rep == 11:
            futoshiki_output.write(str(solution[k]))
        if rep == 12:
            futoshiki_output.write("\n")
        if rep >= 12 and rep < 15:
            futoshiki_output.write(str(solution[k]) + ", ")
        if rep == 15:
            futoshiki_output.write(str(solution[k]))
        rep += 1
