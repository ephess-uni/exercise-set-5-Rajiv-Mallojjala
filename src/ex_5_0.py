"""ex_5_0.py"""
def line_count(infile):
    with open(infile) as f:
        lines = f.readlines()
        num_lines = len(lines)
        print("Number of lines in file {}: {}".format(infile, num_lines))


if __name__ == "__main__":
    line_count("example.txt")

    from pathlib import Path
    data_directory = Path("data")
    line_count(data_directory / "ex_5_2-data.csv")
