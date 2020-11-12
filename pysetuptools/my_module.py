import yaml
import numpy as np
from pathlib import Path

# read yaml
def count_matrix():
    path = Path(__file__).parent / "data/dummy.yaml"
    with open(path, 'r') as configs:
        configs = yaml.load(configs, yaml.FullLoader)

    # now get the matrix size
    size = configs["matrix_size"]

    matrix = np.ones(shape=(size, size))

    # now let's just print the sum of the matrix
    return np.sum(matrix)
