i = 9
while i >= 1:
    j = 1
    while i >= j:
        print("{:d}*{:d}={:2d}".format(j, i, i * j), end=' ')
        j += 1
    print()
    i -= 1


