from os import remove

import Tools
import aocd



PASS = 3
with open('inputs/session.txt') as f:
    session = f.read()

test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

data = Tools.input_as_lines(aocd.get_data(session, day=2))
# data = Tools.input_as_lines(test)

def convert_int(d):
    temp = []
    for line in d:
        temp_line = []
        line_list = line.split()
        for l in line_list:
            temp_line.append(int(l))
        temp.append(temp_line)
    return temp

data = convert_int(data)


def check_line(line):
    increase = None
    line_length = len(line)
    for ii in range(line_length):
        if ii < line_length - 1:
            dif = int(line[ii]) - int(line[ii + 1])
            if 0 < abs(dif) <= PASS:
                if increase == None:
                    increase = dif > 0
                else:
                    temp_dir = dif > 0
                    if increase != temp_dir:
                        # print("fail change dir")
                        return ii
            else:
                return ii
    return True

total = 0
for i, line in enumerate(data):
    length = len(line)
    print("line to test " + str(line))
    attempt = False
    result = check_line(line)
    if type(result) == int:
        for i in range(length):
            test = line.copy()
            test.pop(i)
            r = check_line(test)
            if type(r) == int:
                print("not working" + str(i))
            else:
                print("worked with " + str(i))
                total += 1
                break
    else:
        print("pass")
        total += 1
print(total)


