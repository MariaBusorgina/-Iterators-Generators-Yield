nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# Task_1
class FlatIterator:

    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.cont_iter = -1
        self.list_in_list = []

    def __iter__(self):
        return self

    def __next__(self):
        self.list_in_list = sum(self.iter_list, [])
        if len(self.list_in_list) - 1 == self.cont_iter:
            raise StopIteration
        else:
            self.cont_iter = self.cont_iter + 1
            return self.list_in_list[self.cont_iter]


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# Task_2
def flat_generator(nested_list):
    count = 0
    while len(nested_list) > count:
        for item in nested_list[count]:
            yield item
        count += 1


for item in flat_generator(nested_list):
    print(item)
