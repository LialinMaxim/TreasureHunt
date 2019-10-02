from main_func import NO_FOUND_MESSAGE, FOUND_MESSAGE


class TreasureHunt():
    def __init__(self, map_str):
        self.map_str = map_str
        self.map = self.transform(map_str)
        self.result = []
        self.treasure_item = None
        self.message = None

    def __str__(self):
        return '\n'.join([' '.join(r) for r in self.map])

    @staticmethod
    def transform(map_str):
        return [r.split() for r in map_str.split('\n') if r]

    def get_next_item(self, item):
        first, second = int(item[0]), int(item[1])
        new_item = self.map[first - 1][second - 1]
        if item == new_item:
            self.treasure_item = new_item
        return new_item

    def go_hunt(self, item='11'):
        self.result = []
        self.treasure_item = None
        self.message = None

        while True:
            if item not in self.result:
                self.result.append(item)
                item = self.get_next_item(item)
            else:
                if self.treasure_item:
                    self.message = FOUND_MESSAGE
                else:
                    self.message = NO_FOUND_MESSAGE
                return self.result
