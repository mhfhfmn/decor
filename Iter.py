from decor import logger

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, some_list):
        self.my_list = some_list


    def __iter__(self):
        self.my_list_cursor = -1
        self.nested_list_cursor = 0
        return self


    def __next__(self):
        self.my_list_cursor += 1
        if self.my_list_cursor == len(self.my_list[self.nested_list_cursor]):
            self.my_list_cursor = 0
            self.nested_list_cursor += 1
        if self.nested_list_cursor == len(self.my_list):
            raise StopIteration
        return self.my_list[self.nested_list_cursor][self.my_list_cursor]


@logger
def main():
    for elem in FlatIterator(nested_list):
        print(elem)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

if __name__ == '__main__':
    main()