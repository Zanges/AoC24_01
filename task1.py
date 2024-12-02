INPUT_FILE = "input.txt"


def load(filename: str) -> tuple[list[int], list[int]]:
    """
    Load the data from the file and return the left and right lists.

    :param filename: file to load

    :return: tuple with left and right lists
    """
    with open(filename, "r") as fileobj:
        lines = fileobj.readlines()
    left_list = []
    right_list = []
    for line in lines:
        line = line.strip()
        left, right = line.split(" " * 3)
        left_list.append(int(left))
        right_list.append(int(right))
    left_list.sort()
    right_list.sort()
    return left_list, right_list


def find_distance(element1: int, element2: int) -> int:
    """
    Find the distance between two elements.

    :param element1: first element
    :param element2: second element

    :return: distance between the two elements
    """
    return abs(element1 - element2)


def find_list_distance(left_list: list[int], right_list: list[int]) -> int:
    """
    Find the distance between two lists.

    :param left_list: first list
    :param right_list: second list

    :return: distance between the two lists
    """
    distance = 0
    for left, right in zip(left_list, right_list):
        distance += find_distance(int(left), int(right))
    return distance


def main():
    left_list, right_list = load(INPUT_FILE)
    distance = find_list_distance(left_list, right_list)
    print(distance)


if __name__ == "__main__":
    main()