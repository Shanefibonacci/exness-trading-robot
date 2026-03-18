def moving_average(data, window_size):
    """
    Calculate the moving average of a given data series.
    
    Parameters:
    data (list): A list of numerical values.
    window_size (int): The size of the moving window.
    
    Returns:
    list: A list containing the moving averages.
    """
    if window_size <= 0:
        raise ValueError('Window size must be a positive integer')
    if window_size > len(data):
        raise ValueError('Window size must not be greater than the length of the data')

    moving_averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        window_average = sum(window) / window_size
        moving_averages.append(window_average)

    return moving_averages
