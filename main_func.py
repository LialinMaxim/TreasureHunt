FOUND_MESSAGE = "Treasure FOUND"
NO_FOUND_MESSAGE = "Treasure NOT Found"


def transform(data):
    return [r.split() for r in data.split('\n') if r]


def go_hunt(map_str, start='11', ):
    result = []
    _map = transform(map_str)

    def _next_item(item):
        if item not in result:
            result.append(item)
            k, v = int(item[0]), int(item[1])
            new_item = _map[k - 1][v - 1]
            if item == new_item:
                return FOUND_MESSAGE
            return _next_item(new_item)
        else:
            return NO_FOUND_MESSAGE

    message = _next_item(start)
    return result, message


if __name__ == '__main__':
    print("Start Func Test")
