from itertools import chain
from decor import logger_with_path


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(ls: list):
    res = [elem for elem in chain(*ls)]
    for obj in res:
        yield obj

@logger_with_path(path = 'logs\logs.log')
def main():
    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    return flat_list


if __name__ == "__main__":
    main()