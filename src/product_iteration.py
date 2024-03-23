class ProductIteration:
    category = list

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        self.current_value += 1
        if self.current_value < len(self.category):
            return self.category[self.current_value]
        else:
            raise StopIteration
