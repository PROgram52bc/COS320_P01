import fileinput

lines = [ line.strip(' \n') for line in fileinput.input() ]

goal = int(lines[0])
limits = [ int(n) for n in lines[2:] ]

nPasses = 0
iCurr = 0
while True:
    # if the current player cannot throw, impossible
    if limits[iCurr] == 0:
        nPasses = 0
        break

    limitCurr = iCurr+limits[iCurr] # The furthest player that can be thrown to
    # if can throw pass the goal, done
    if limitCurr >= goal:
        nPasses += 1
        break

    # find the next best player among iCurr+1 ... limitCurr
    iCurr = max(range(iCurr+1, limitCurr+1),
            key=lambda iNext: iNext+limits[iNext])
    nPasses += 1


print(nPasses if nPasses != 0 else "Impossible")
