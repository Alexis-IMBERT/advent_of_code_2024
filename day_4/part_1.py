from pathlib import Path
import re
from tqdm import tqdm
import numpy as np


def main(file_name: str):
    data = Path(file_name).read_text(encoding="utf-8")
    matrix = convert_data_to_matrix(data)
    regex = r"(?=(XMAS|SAMX))"
    horizontal_count = len(re.findall(regex, data))
    vertical_count = len(re.findall(regex, convert_matrix_to_data(matrix.T)))
    diagonal_top_left_to_bottom_right = len(
        re.findall(regex, "\n".join(get_list_of_diagonals(matrix)))
    )
    diagonal_bottom_left_to_top_right = len(
        re.findall(regex, "\n".join(get_list_of_diagonals(np.flip(matrix, axis=1))))
    )
    print(
        horizontal_count
        + vertical_count
        + diagonal_top_left_to_bottom_right
        + diagonal_bottom_left_to_top_right
    )


def convert_data_to_matrix(data: str):
    return np.array([list(line) for line in data.split("\n")])


def convert_matrix_to_data(matrix: np.ndarray):
    return "\n".join(["".join(x) for x in matrix])


def get_list_of_diagonals(matrix: np.ndarray):
    diagonals = []
    for i in tqdm(range(matrix.shape[0])):
        diagonals.append("".join(list(matrix.diagonal(i))))
        diagonals.append("".join(list(matrix.diagonal(-i))))
    return diagonals


if __name__ == "__main__":
    main(file_name="day_4/data.txt")
