""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

def process_data(infile, outfile):
    # Load the data from the input file
    data = np.loadtxt(infile, delimiter=",")

    # Shift the data to have a mean of 0
    shifted = data - np.mean(data, axis=0)

    # Scale the data to have a standard deviation of 1
    scaled = shifted / np.std(shifted, axis=0)

    # Save the processed data to the output file
    np.savetxt(outfile, scaled, delimiter=",")

if __name__ == "__main__":
    # Create the argument parser object
    parser = ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")

    # Add the input and output file arguments
    parser.add_argument("infile", help="Input file of data to be processed")
    parser.add_argument("outfile", help="Output file for processed data")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Call the process_data function with the input and output filenames
    process_data(args.infile, args.outfile)
