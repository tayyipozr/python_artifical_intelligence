import csv
import math
import operator
import matplotlib.pyplot as plt

# initialize knn class
class Knn:
    def __init__(self, phones):
        self.phones = phones
        self.length = len(phones)

    # calculation of euclideanDistance between two phone properties
    @staticmethod
    def euclideanDistance(phone1, phone2):
        d = 0
        for i in range(len(phone1)):
            d += pow((phone1[i] - phone2[i]), 2)
        d = math.sqrt(d)
        return d

    def findNeighbours(self, test_phone, knn_k):
        distances = {}
        neighbours = []
        for k, v in self.phones.items():
            euclideanDistance = self.euclideanDistance(v.properties, test_phone.properties)
            print(euclideanDistance)
            distances[k] = euclideanDistance
        sorted_distances = sorted(distances.items(), key=operator.itemgetter(1))
        for i, phone in enumerate(sorted_distances):
            if i < knn_k + 1:
                neighbours.append(phone)
            else:
                break
        return neighbours


# initialize phone class
class Phone:
    def __init__(self, properties):
        self.properties = properties


# initialize train dictionary
train_dict = {}

# initialize test dictionary
test_dict = {}

with open("train.csv", "r", encoding="utf8") as csvFile:
    reader = csv.reader(csvFile)
    for i, line in enumerate(reader):
        if i > 0:
            phone = Phone(line)
            for k, j in enumerate(phone.properties):
                phone.properties[k] = float(j)
                train_dict[i] = phone

with open("test.csv", "r", encoding="utf8") as csvFile:
    reader = csv.reader(csvFile)
    for i, line in enumerate(reader):
        if i > 0:
            phone = Phone(line)
            for k, j in enumerate(phone.properties):
                phone.properties[k] = float(j)
                test_dict[i] = phone

knn = Knn(train_dict)
test_phone_input = int(input("Select a number to pick a test phone (between 1-1000) : "))
acc = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for a in num:
    print(a)
    neighbours = knn.findNeighbours(test_dict[test_phone_input], a)
    guesses = []
    for i in neighbours:
        for k, v in train_dict.items():
            if i[0] == k:
                print(v.properties[-1])
                guesses.append(v.properties[-1])
    print("-----------")
    print(test_dict[test_phone_input].properties[-1])

    print(guesses)

    accuracy = 0
    for i in guesses:
        if test_dict[test_phone_input].properties[-1] == i:
            accuracy += 1
    print("Accuracy: " + str(accuracy / len(neighbours) * 100))
    acc.append(accuracy / len(neighbours) * 100)

print(num)
print(acc)
f = plt.figure()
plt.xticks(num)
y = list(range(0, 101, 5))
plt.yticks(y)
plt.plot(num, acc)
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.show()
f.savefig("plot.pdf")
