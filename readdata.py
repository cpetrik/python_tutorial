def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
    """
    Reads data from CU Boulder Weather Station data file
    Parameters:
        columns: dictionary of column names mapped to column indices
        types: dictionary of column names mapped to the types to which to 
               convert each column of data
        filename: string path pointing to the CU Boulder Weather Station file
    """

    # Initialize data variable
    data = {}
    for column in columns:
        data[column] = []

    # Read the data file
    with open(filename,'r') as datafile:

        # Read first 3 lines (header)
        for _ in range(3):
            datafile.readline()

        # Read and parse the rest of the file
        for line in datafile:
            split_line = line.split()
            for column in columns:
                i = columns[column]
                t = types.get(column,str)
                value = t(split_line[i])
                data[column].append(value)

    return data
