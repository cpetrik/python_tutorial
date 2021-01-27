def print_comparison(name, dates, times, orig_data, comp_data):
    """
    Print a comparison of two time series (original and computed)
    Parameters:
        name: string name for the data being compared (limited to 9 char)
        dates: list of strings representing dates for each data
        orig_data: list of original data (floats)
        comp_data: list of computed data (floats)
    """

    # Output comparison of data
    print('                ORIGINAL  COMPUTED')
    print(f' DATE    TIME {name.upper():>9} {name.upper():>9} DIFFERENCE')
    print('------- ------ --------- --------- ----------')
    zip_data = zip(dates, times, orig_data, comp_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {diff:10.6f}')


