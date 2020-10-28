# Initialize data variable
data = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename,'r') as datafile:
    # Read first 3 lines (header)
    for _ in range(3):
        print(_)
        datafile.readline()
    # Read and parse the rest of the file
    # creates a list of list of strings
    for line in datafile:
        datum = line.split()
        data.append(datum)

# DEBUG

