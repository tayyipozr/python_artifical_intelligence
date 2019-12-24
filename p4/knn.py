import csv
import math
import operator
import matplotlib.pyplot as plt


# initialize knn class
class Knn:
    def __init__(self, test_phones, train_phones):
        self.train_phones = train_phones
        self.test_phones = test_phones
        print("The nearest ten neighbours searching started...")
        self.neighbours = self.findNeighbours()
        print("Founded")

    # calculation of euclideanDistance between two phone properties
    @staticmethod
    def euclideanDistance(phone1, phone2):
        d = 0
        for i in range(len(phone1)):
            d += pow((phone1[i] - phone2[i]), 2)
        d = math.sqrt(d)
        return d

    def findNeighbours(self):
        top_ten_neighbours = {}
        neighbours = {}
        for k, v in self.train_phones.items():
            for key, value in self.test_phones.items():
                euclideanDistance = self.euclideanDistance(v.properties, value.properties)
                neighbours[value] = euclideanDistance
            sorted_neighbours = sorted(neighbours.items(), key=operator.itemgetter(1))
            top_ten_neighbours[v] = sorted_neighbours[:10]
        return top_ten_neighbours

    def accuracy(self, knn_k):
        accuracy = 0
        for key, value in self.neighbours.items():
            acc = 0
            counter = 0
            for v in value:
                if counter == knn_k:
                    break
                if key.label == v[0].label:
                    acc += 1
                counter += 1
            accuracy += (acc / counter)
        return accuracy


# initialize phone class
class Phone:
    def __init__(self, properties):
        self.label = properties[-1]
        self.properties = properties[:20]


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

print("It started\nPlease wait....")
knn = Knn(test_dict, train_dict)
knn_acc = []
for i in range(1, 11):
    knn_acc.append(knn.accuracy(i))

plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], knn_acc)
plt.show()
