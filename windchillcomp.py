from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_windchill

# Create a column dictionary (names and indices to read)
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each colun (only if not string)
types = {'tempout':float, 'windspeed':float, 'windchill':float}

# Read the data file
data = read_data(columns, types=types)

# Compute windchill index
windchill = [compute_windchill(t,w) for t, w in zip(data['tempout'],data[windspeed])]
# Running the function to compute wci

# Output comparison of data
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'],
    windchill)

#DEBUG

