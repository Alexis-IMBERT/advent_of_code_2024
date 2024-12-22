from pathlib import Path

from dataclasses import dataclass
from networkx import DiGraph


@dataclass
class UpdateOrder:
    page: int
    dependancy: int


def main(file_name: str):
    graph_dependancies, updates = loading_data(file_name)
    print(
        "Partie 1 :",
        sum(
            get_middle_elements(
                filter_valid_updates(graph_dependancies, updates),
            ),
        ),
    )
    print(
        "Partie 2 :",
        sum(
            get_middle_elements(
                correct_updates(
                    graph_dependancies,
                    filter_invalid_updates(graph_dependancies, updates),
                ),
            )
        ),
    )


def correct_updates(graph_dependancies, invalid_updates):
    return map(
        lambda update_to_correct: correct_update(update_to_correct, graph_dependancies),
        invalid_updates,
    )


def filter_valid_updates(graph_dependancies, updates):
    return list(filter(lambda x: is_valide(x, graph_dependancies), updates))


def filter_invalid_updates(graph_dependancies, updates):
    return list(
        filter(
            lambda update: not is_valide(update, graph_dependancies),
            updates,
        )
    )


def get_middle_elements(listes: list[list[int]]) -> list[int]:
    return map(lambda liste: liste[(len(liste) // 2)], listes)


def loading_data(file_name):
    data = Path(file_name).read_text(encoding="utf-8").split("\n\n")
    graph_dependancies = DiGraph()
    updates = list(map(lambda x: [eval(y) for y in x.split(",")], data[1].split("\n")))
    graph_dependancies.add_edges_from(
        map(
            lambda x: [x.dependancy, x.page],
            map(
                lambda x: UpdateOrder(eval(x.split("|")[0]), eval(x.split("|")[1])),
                data[0].split("\n"),
            ),
        )
    )
    return graph_dependancies, updates


def is_valide(update: list[int], graphe: DiGraph) -> bool:
    all_depandance = []
    nodes = graphe.nodes()
    for element in update:
        if element in nodes:
            depandance = list(graphe.neighbors(element))
            all_depandance.extend(depandance)
        if element in all_depandance:
            return False
    return True


def correct_update(update: list[int], graphe: DiGraph) -> list[int]:
    all_dependance = []
    corrected_update = []
    nodes = graphe.nodes()
    for element in update:
        if element in nodes:
            all_dependance.extend(list(graphe.neighbors(element)))
        corrected_update.insert(
            (
                max(
                    [
                        corrected_update.index(predecessor)
                        for predecessor in list(graphe.predecessors(element))
                        if predecessor in corrected_update
                    ],
                    default=-1,
                )
                + 1
                if element in all_dependance
                else 0
            ),
            element,
        )
    return corrected_update


if __name__ == "__main__":
    main(file_name="day_5/data.txt")
