import csv


stats = []



def read_data():
    stats = []
    with open("Data/stats.csv") as stats_file:
        reader = csv.reader(stats_file,delimiter=",")
        for row in reader:
            stats.append(row)
    return stats

def calculate_first(data,name):
    first_list = {}
    for row in data:
        if row[2] == name or row[3] == name:
            if row[4] == "A":
                name = row[2]
            else:
                name = row[3]
            if name not in first_list.keys():
                    first_list[name] = 1
            else:
                    first_list[name] += 1
    print(first_list)
    

def calculateSweeps(data,name):
    sweeps = 0
    for row in data:
        if row[9] == row[10] and row[9] != name and (row[2] == name or row[3] == name):
            print(row[2] + ", " + row[3])
            sweeps += 1
    print(sweeps)


def main():
    stats = read_data()
    del stats[0] #remove first list
    calculate_first(stats,"Nelson Salahub")
    calculateSweeps(stats,"Benjamin Wheeler")

if __name__ == "__main__":
    main()
