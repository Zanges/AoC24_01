from task1 import load, INPUT_FILE


def calculate_similarity(left_list: list[int], right_list: list[int]) -> int:
    """
    Calculate the similarity between two lists.

    :param left_list: first list
    :param right_list: second list

    :return: similarity between the two lists
    """
    similarity = 0
    for left in left_list:
        similarity += left * right_list.count(left)
    return similarity


def main():
    left_list, right_list = load(INPUT_FILE)
    similarity = calculate_similarity(left_list, right_list)
    print(similarity)


if __name__ == "__main__":
    main()