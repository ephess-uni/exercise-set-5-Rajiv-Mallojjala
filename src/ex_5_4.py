"""ex_5_4.py"""
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

# Use these predefined paths. Note: automated tests expect these paths
# Changing these paths will cause tests to fail.

root_dir = get_repository_root()
data_dir = root_dir / "data"
output_dir = root_dir / "outputs"
input_file = data_dir / "ex_5_4-data.csv"
output_file = output_dir / "ex_5_4-processed.csv"

# Load data from input file
data = np.loadtxt(input_file, delimiter=",")

# Set negative elements to 0
data[data < 0] = 0

# Save processed data to output file
np.savetxt(output_file, data, delimiter=",")
