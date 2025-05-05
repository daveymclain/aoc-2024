from typing import List
import time


def input_as_string(filename: str) -> str:
    """returns the content of the input file as a string"""
    # with open(filename) as f:
    return filename.rstrip("\n")


def input_as_lines(filename: str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")


def input_as_ints(filename: str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))


class Timer:
    def __init__(self):
        self.start = time.time()

    def stop(self, dec_place=4):
        time_taken = round(time.time() - self.start, dec_place)
        print(f"Time taken {time_taken}")
        return time_taken


def decorator(part):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"part {part} = {func(*args, **kwargs)}")

        return wrapper

    return decorator


@decorator(2)
def test():
    print("test")
    return 1231


if __name__ == "__main__":
    timer = Timer()
    # time.sleep(2.4532)

    test()

    timer.stop()


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'