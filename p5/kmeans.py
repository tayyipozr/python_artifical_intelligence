import matplotlib.pyplot as plt
import random
from math import sqrt
from time import sleep


class Person:
    def __init__(self, income, spend):
        self.spend = spend
        self.income = income

    def setSpend(self, spend):
        self.spend = spend

    def setIncome(self, income):
        self.income = income


people = []

with open("data.txt", "r") as File:
    counter = 0
    for row in File:
        row = row.strip().split(',')
        if counter > 0:
            p = Person(int(row[0]), int(row[1]))
            people.append(p)
        counter += 1


def findMid(alist):
    income = 0
    spend = 0
    for person in alist:
        income += person.income
        spend += person.spend
    p = income / len(alist), spend / len(alist)
    return p


def randomP():
    p1 = Person(random.randrange(50, 200), random.randrange(30, 100))
    p2 = Person(random.randrange(210, 350), random.randrange(30, 100))
    return p1, p2


rnd = randomP()


def euclideanDistance(person1, person2):
    income = pow((person1.income - person2.income), 2)
    spend = pow((person1.spend - person2.spend), 2)
    d = (sqrt(income) + sqrt(spend))
    return d


def findNearests(alist, innerRnd):
    distancep1 = []
    distancep2 = []
    for person in alist:
        if euclideanDistance(innerRnd[0], person) > euclideanDistance(innerRnd[1], person):
            distancep2.append(person)
        else:
            distancep1.append(person)
    return distancep1, distancep2


nearest = findNearests(people, rnd)

plt.xlabel("Income")
plt.ylabel("Spend")
plt.scatter([person.income for person in people], [person.spend for person in people])
plt.scatter(rnd[0].income, rnd[0].spend, color='red')
plt.scatter(rnd[1].income, rnd[1].spend, color='black')
plt.show()
plt.close('Figure 1')
plt.scatter([person.income for person in nearest[0]], [person.spend for person in nearest[0]], color='red')
plt.scatter([person.income for person in nearest[1]], [person.spend for person in nearest[1]], color='black')
plt.show()
plt.close()

previousRnd = [0, 0]
previousRnd2 = [0, 0]

while (previousRnd[0] != rnd[0].income and previousRnd[1] != rnd[0].spend) and (previousRnd2[0] != rnd[1].income and
                                                                                previousRnd2[1] != rnd[1].spend):
    previousRnd[0] = rnd[0].income
    previousRnd[1] = rnd[0].spend
    previousRnd2[0] = rnd[1].income
    previousRnd2[1] = rnd[1].spend

    incomeSpend1 = findMid(nearest[0])
    rnd[0].income = incomeSpend1[0]
    rnd[0].spend = incomeSpend1[1]
    incomeSpend2 = findMid(nearest[1])
    rnd[1].income = incomeSpend2[0]
    rnd[1].spend = incomeSpend2[1]
    nearest = findNearests(people, rnd)
    print(f"Previous red dot x: {previousRnd[0]} y: {previousRnd[1]}")
    print(f"Previous black dot x: {previousRnd2[0]} y: {previousRnd2[1]}")
    print(f"Red dot x: {rnd[0].income} y: {rnd[0].spend}")
    print(f"Black dot x: {rnd[1].income} y: {rnd[1].spend}")
    print("-" * 50)
    plt.xlabel("Income 2")
    plt.ylabel("Spend 2")
    plt.scatter([person.income for person in people], [person.spend for person in people])
    plt.scatter(rnd[0].income, rnd[0].spend, color='red')
    plt.scatter(rnd[1].income, rnd[1].spend, color='black')
    plt.show()
    plt.close()
    plt.scatter([person.income for person in nearest[0]], [person.spend for person in nearest[0]], color='red')
    plt.scatter([person.income for person in nearest[1]], [person.spend for person in nearest[1]], color='black')
    plt.show()
    plt.close()
