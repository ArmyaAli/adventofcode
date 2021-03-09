file_name = "input.txt"

f = open(file_name, "r")

def report_repair_part_1():
    contents = f.read().splitlines()

    # first pass
    solution = -1
    for entry in contents:
        for secondpass in contents:
            sum = int(entry) + int(secondpass)
            if sum == 2020:
                solution = int(entry) * int(secondpass)
                break

def report_repair_part_2():
    contents = f.read().splitlines()
    solution = -1
    for entry in contents:
        for secondpass in contents:
            for thirdpass in contents:
                sum = int(entry) + int(secondpass) + int(thirdpass)
                if sum == 2020:
                    solution = int(entry) * int(secondpass) * int(thirdpass)
                    break
