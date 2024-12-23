from pathlib import Path


def main(input_file_path="day_6/input.txt"):
    room = Room(input_file_path)
    room.solve_1()


class Room:
    def __init__(self, file_path: str):
        self.room = load_data(file_path)
        self.guard_pos = find_guard(self.room)
        # room size
        self.n = len(self.room)
        self.m = len(self.room[0])

    @property
    def turn_guard(self):
        return {
            "^": ">",
            ">": "v",
            "v": "<",
            "<": "^",
        }

    @property
    def get_next_case(self):
        return {
            "^": lambda i, j: (i - 1, j) if i > 0 else None,
            ">": lambda i, j: (i, j + 1) if j < self.m - 1 else None,
            "v": lambda i, j: (i + 1, j) if i < self.n - 1 else None,
            "<": lambda i, j: (i, j - 1) if j > 0 else None,
        }

    def count_path(self):
        count = 0
        for line in self.room:
            for char in line:
                if char == "X":
                    count += 1
        return count

    def move(self):
        i, j = self.guard_pos
        next_case = self.get_next_case[self.room[i][j]](i, j)
        if next_case is None:
            self.room[i][j] = 'X'
            self.guard_pos = None
            return
        next_i, next_j = next_case
        if self.room[next_i][next_j] == "#":
            self.room[i][j] = self.turn_guard[self.room[i][j]]
        else:
            self.room[next_i][next_j], self.room[i][j] = self.room[i][j], "X"
            self.guard_pos = next_case

    def solve_1(self):
        while self.guard_pos:
            self.move()
        print(self.count_path())
    
    # def solve_2(self):
    # placer l'obstacle sur le prochain endroit
    # vérifier si on a un cycle
    # si on a un cycle, on a un nombre de cycle
    


def load_data(input_file_path):
    brut_data = Path(input_file_path).read_text(encoding="utf-8").split("\n")
    room = [list(i) for i in brut_data]
    return room


def find_guard(data):
    for i, line in enumerate(data):
        if "^" in line:
            return (i, line.index("^"))
    return None


if __name__ == "__main__":
    main()
