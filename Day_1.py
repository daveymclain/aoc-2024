from os.path import split

import Tools
import aocd



with open('inputs/session.txt') as f:
    session = f.read()

test = """3   4
4   3
2   5
1   3
3   9
3   3"""

data = Tools.input_as_lines(aocd.get_data(session, day=1))




def make_lists(data):
    list_left = []
    list_right = []
    for line in data:
        l, r = line.split()
        list_left.append(int(l))
        list_right.append(int(r))
    return list_left, list_right

left, right = make_lists(data)

left.sort()
right.sort()

def part_1(l,r):
    length = len(l)
    deviation = 0
    for i in range(length):
        temp = [l[i], r[i]]
        temp.sort()

        deviation += temp[1] - temp[0]

    print(deviation)


part_1(left,right)

# part 2

def dict_of_right(r):
    d = {}

    for n in r:
        if n in d.keys():
            d[n] += 1
        else:
            d[n] = 1
    return d

dict_right =dict_of_right(right)

total = 0

for n in left:
    if n in dict_right.keys():
        total += n * dict_right[n]
print(total)