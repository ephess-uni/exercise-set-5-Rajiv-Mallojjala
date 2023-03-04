""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np
data = np.random.normal(size=(100, 5))


try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # TODO: Center the data by subtracting the mean of each column
    data_mean = np.mean(data, axis=0)
    centered = data - data_mean
    # TODO: Standardize the data by dividing each column by its standard deviation
    data_std = np.std(centered, axis=0)
    processed = centered / data_std

    # Save the processed data to a file
    np.savetxt('processed_data.txt', processed, fmt='%.3f')
