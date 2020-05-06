import sys
import random

if len(sys.argv) != 4:
    print("Usage: python3 {} [goal] [min] [max]".format(sys.argv[0]))
    print("Generate input values with uniform distributions")
    sys.exit()

goal, minNum, maxNum = [ int(num) for num in sys.argv[1:] ]

print(goal)
print()
for _ in range(goal):
    print(random.randint(minNum, maxNum))
