import Tools
import aocd

with open('inputs/session.txt') as f:
    session = f.read()

test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

data = Tools.input_as_lines(aocd.get_data(session, day=2))


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

def check_gaps(d, p):
    remove_list = []
    for i, line in enumerate(d):
        increase = None
        line_length = len(line)
        for ii in range(line_length):
            if ii < line_length - 1:
                dif = int(line[ii]) - int(line[ii + 1])
                if abs(dif) == 0:
                    # print("fail same")
                    remove_list.append(i)
                    break
                if abs(dif) <= p:
                    if increase == None:
                        increase = dif > 0
                    else:
                        temp_dir = dif > 0
                        if increase != temp_dir:
                            # print("fail change dir")
                            remove_list.append(i)
                            break
                else:
                    # print("fail number to big")
                    remove_list.append(i)
                    break
    remove_list.reverse()
    for i in remove_list:
        d.pop(i)

    return d


PASS = 3
safe = 0

data = check_gaps(data,PASS)
print(len(data))
