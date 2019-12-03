import random

with open("c.txt", "r") as f:
    c = f.readline()
    c = int(c)

fv = []
with open("v.txt", "r") as f:
    for v in f:
        fv.append(int(v))

fw = []
with open("w.txt", "r") as f:
    for w in f:
        fw.append(int(w))


class Knapsack:
    def __init__(self, c, fw, fv, popSize, parentSelection, n, mutProb, elitism):
        self.fw = fw
        self.fv = fv
        self.mutProb = mutProb
        self.c = c
        self.n = n
        self.averageFitness = self.averageFitness()
        self.popSize = popSize
        self.population = self.initilizePop()
        self.selectedParents = self.selectParents(parentSelection)
        self.fittest = self.pickElite()

    def pickElite(self):
        if elitism:
            max = 0
            chrom = self.selectedParents[0]
            for chromosome in self.population:
                if chromosome.getWeight() <= c and chromosome.getValue() > max:
                    max = chromosome.getValue()
                    chrom = chromosome
            return chrom
        else:
            return None

    def averageFitness(self):
        totalValue = 0
        for value in self.fv:
            totalValue += value
        totalValue /= 3
        return totalValue

    def initilizePop(self):
        temp = []
        for i in range(popSize):
            temp.append(self.Chromosome())
        return temp

    def selectParents(self, numberOfSelection):
        selectedParents = {}
        selectedParents2 = []
        totalValue = 0
        for chromosome in self.population:
            if chromosome.fitness() != 0:
                totalValue += chromosome.getValue()
                selectedParents[chromosome] = chromosome.getValue()
        newSelectedParents = self.sortDictDueToValues(selectedParents)
        if numberOfSelection == 1:
            for i in range(len(selectedParents)):
                rnNum = random.randrange(totalValue)
                total = 0
                for j in newSelectedParents:
                    total += j.getValue()
                    if total > rnNum:
                        selectedParents2.append(j)
                        break
        if numberOfSelection == 2:
            pass
        return selectedParents2

    def sortDictDueToValues(self, adict):
        alist = list(adict.values())
        alist.sort()
        newSelectedParents = []
        for value in alist:
            for k, v in adict.items():
                if value == v:
                    newSelectedParents.append(k)
        return newSelectedParents

    def crossingOver(self):
        for i in range(0, len(self.selectedParents), 2):
            if self.n == 1 and i + 1 < len(self.selectedParents) > 1:
                beginingeOfFirst = self.selectedParents[i].chromosome[:int(len(self.selectedParents[i].chromosome) / 2)]
                endOfSecond = self.selectedParents[i + 1].chromosome[int(len(self.selectedParents[i].chromosome) / 2):]
                beginingeOfSecond = self.selectedParents[i + 1].chromosome[
                                    :int(len(self.selectedParents[i].chromosome) / 2)]
                endOfFirst = self.selectedParents[i].chromosome[int(len(self.selectedParents[i + 1].chromosome) / 2):]
                self.selectedParents[i].chromosome = beginingeOfFirst + endOfSecond
                self.selectedParents[i + 1].chromosome = beginingeOfSecond + endOfFirst
            elif self.n == 2 and i + 1 < len(self.selectedParents) > 1:
                beginingeOfFirst = self.selectedParents[i].chromosome[:int(len(self.selectedParents[i].chromosome) / 3)]
                middleOfFirst = self.selectedParents[i].chromosome[int(len(self.selectedParents[i].chromosome) / 3):int(
                    (len(self.selectedParents[i].chromosome) / 3) * 2)]
                endOfFirst = self.selectedParents[i].chromosome[(int(len(self.selectedParents[i].chromosome) / 3) * 2):]
                beginingeOfSecond = self.selectedParents[i + 1].chromosome[
                                    :int(len(self.selectedParents[i + 1].chromosome) / 3)]
                middleOfSecond = self.selectedParents[i + 1].chromosome[
                                 int(len(self.selectedParents[i + 1].chromosome) / 3):int(
                                     (len(self.selectedParents[i + 1].chromosome) / 3) * 2)]
                endOfSecond = self.selectedParents[i + 1].chromosome[
                              int((len(self.selectedParents[i + 1].chromosome) / 3) * 2):]
                self.selectedParents[i].chromosome = beginingeOfFirst + middleOfSecond + endOfFirst
                self.selectedParents[i + 1].chromosome = beginingeOfSecond + middleOfFirst + endOfSecond
            elif self.n == 3 and i + 1 < len(self.selectedParents) > 1:
                beginingeOfFirst = self.selectedParents[i].chromosome[:int(len(self.selectedParents[i].chromosome) / 4)]
                middleFirstOfFirst = self.selectedParents[i].chromosome[
                                     int(len(self.selectedParents[i].chromosome) / 4):int(
                                         (len(self.selectedParents[i].chromosome) / 4) * 2)]
                middleSecondOfFirst = self.selectedParents[i].chromosome[
                                      int((len(self.selectedParents[i].chromosome) / 4) * 2):int(
                                          (len(self.selectedParents[i].chromosome) / 4) * 3)]
                endOfFirst = self.selectedParents[i].chromosome[int((len(self.selectedParents[i].chromosome) / 4) * 3):]
                beginingeOfSecond = self.selectedParents[i + 1].chromosome[
                                    :int(len(self.selectedParents[i + 1].chromosome) / 4)]
                middleFirstOfSecond = self.selectedParents[i + 1].chromosome[
                                      int(len(self.selectedParents[i + 1].chromosome) / 4):int(
                                          (len(self.selectedParents[i + 1].chromosome) / 4) * 2)]
                middleSecondOfSecond = self.selectedParents[i + 1].chromosome[
                                       int((len(self.selectedParents[i + 1].chromosome) / 4) * 2):int(
                                           (len(self.selectedParents[i + 1].chromosome) / 4) * 3)]
                endOfSecond = self.selectedParents[i + 1].chromosome[
                              int((len(self.selectedParents[i + 1].chromosome) / 4) * 3):]
                self.selectedParents[
                    i].chromosome = beginingeOfFirst + middleFirstOfSecond + middleSecondOfFirst + endOfSecond
                self.selectedParents[
                    i + 1].chromosome = beginingeOfSecond + middleFirstOfFirst + middleSecondOfSecond + endOfFirst
        return self.selectedParents

    def mutation(self):
        includeFittest = False
        for chromosome in self.selectedParents:
            rnNum = random.random()
            print(rnNum)
            if rnNum <= 1 * mutProb:
                print("mutated")
                if chromosome.chromosome[int(rnNum * 15)] == 0:
                    chromosome.chromosome[int(rnNum * 15)] = 1
                else:
                    chromosome.chromosome[int(rnNum * 15)] = 0
            self.population.append(chromosome)
            if self.fittest == chromosome:
                includeFittest = True
        if not includeFittest:
            self.population.append(self.fittest)
        return self.selectedParents

    # def survivalSelection(self, numofsurvivalselection):
    #     if numofsurvivalselection == 2:
    #         self.selectParents(1)
    #         for i in self.selectedParents:
    #             i.increaseAge()
    #         return self.selectedParents
    #     if numofsurvivalselection == 1:
    #
    #
    #

    class Chromosome:
        def __init__(self):
            self.fw = fw
            self.fv = fv
            self.chromosome = self.randomGene()
            self.value = self.getValue()
            self.weight = self.getWeight()
            self.age = 0

        def increaseAge(self):
            self.age += 1

        def getAge(self):
            return self.age

        def randomGene(self):
            temp = []
            for j in range(len(self.fw)):
                temp.append(random.randint(0, 1))
            return temp

        def getValue(self):
            totalValue = 0
            for i, gene in enumerate(self.chromosome):
                totalValue += gene * self.fv[i]
            return totalValue

        def getWeight(self):
            totalWeight = 0
            for i, gene in enumerate(self.chromosome):
                totalWeight += gene * self.fw[i]
            return totalWeight

        def fitness(self):
            if self.weight > c:
                return 0
            else:
                return self.value


popSize = int(input('Size of population : '))

genNumber = int(input('Max number of generation : '))
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))
print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))
print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))
elitism = bool(input('Elitism? (Y or N) ').capitalize())

knapsack = Knapsack(c, fw, fv, popSize, parentSelection, n, mutProb, elitism)

print("---------------------initilize pop--------------------------")
for i in knapsack.population:
    print(f"chromosome : {i.chromosome}, value : {i.getValue()}, weight : {i.getWeight()}")

for i in range(genNumber):
    print(f"----------------------selected {i} parents----------------------")

    for i in knapsack.selectedParents:
        print(f"chromosome : {i.chromosome}, value : {i.getValue()}, weight : {i.getWeight()}")

    print("--------------------------fittest---------------------------")

    print(
        f"chromosome : {knapsack.fittest.chromosome}, value : {knapsack.fittest.getValue()}, weight : {knapsack.fittest.getWeight()}")
    print("-------------------------crossover--------------------------")

    for i in knapsack.crossingOver():
        print(f"chromosome : {i.chromosome}, value : {i.getValue()}, weight : {i.getWeight()}")
    print("--------------------------mutation--------------------------")
    for i in knapsack.mutation():
        print(f"chromosome : {i.chromosome}, value : {i.getValue()}, weight : {i.getWeight()}")

    print("--------------------------newpop----------------------------")

    for i in knapsack.population:
        print(f"chromosome : {i.chromosome}, value : {i.getValue()}, weight : {i.getWeight()}")

print(f"{knapsack.fittest}, age : {knapsack.fittest.getAge()}, chromosome : {knapsack.fittest.chromosome}, value : {knapsack.fittest.getValue()}, weight : {knapsack.fittest.getWeight()}")

with open("out.txt", "w") as f:
    f.write(f"chromosome: {str(knapsack.fittest.chromosome)}\n")
    f.write(f"weight:  {knapsack.fittest.getWeight()}\n")
    f.write(f"value: {knapsack.fittest.getValue()}")