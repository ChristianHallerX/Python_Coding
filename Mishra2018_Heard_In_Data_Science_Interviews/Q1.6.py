# Given arrival and departure times of planes, determine minimum number of gates.

arrival = [930, 1115, 1630]
departure = [1145, 1130, 1645]


def platforms(arrival_list=None, departure_list=None):
    countplanes = 0
    mingates = 0
    # i is the arrival list index, j is the departure list index
    i = j = 0

    while i < len(arrival):
        # if an arrival happens before the a departure, then a plane is present
        if arrival[i] < departure[j]:
            countplanes += 1
            # mingates will record the highest number
            mingates = max(mingates, countplanes)
            # move arrival index
            i += 1

        else:
            # if no arrival happens, then a plane departed, move
            countplanes -= 1
            # move departure index
            j += 1
    return mingates


print(platforms(arrival, departure))
