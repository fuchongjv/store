well = -20
jump = 3
down = -2
day = 1

while well < 0:
    print(day)
    well += jump
    if well >= 0:
        break
    well += down
    if well >= 0:
        break
    day += 1
