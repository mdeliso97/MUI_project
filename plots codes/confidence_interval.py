import numpy as np


def confidence_interval(data, confidence):
    # Calculate mean, standard deviation and confidence interval
    n = len(data)
    mean = np.mean(data)
    sem = np.std(data) / np.sqrt(n)  # sample standard deviation
    lower_bound = mean - confidence * sem
    upper_bound = mean + confidence * sem

    margin_of_error = confidence * sem

    return lower_bound, upper_bound, margin_of_error, mean
