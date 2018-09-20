# In 20x20, we have 20 + 20 = 40 moves
# Like 40 layer binary tree

'''
class tree:

    def __init__(self, coord, depth):
        self.coord = coord
        self.depth = depth
        if self.isValid():
            nodes.add(self)
        print("node with coord", coord, "and depth", depth, "added to nodes")
        print("set contains", len(nodes))
        self.r = None
        self.l = None
        if 40 - self.depth <= abs(self.coord):
            # can't get back
            pass
        else:
            self.makeChildren()

    def isValid(self):
        return self.coord == 0 and self.depth == 40

    def makeChildren(self):
        if self.depth >= 40:
            pass
        else:
            self.r = tree(self.coord + 1, self.depth + 1)
            self.l = tree(self.coord - 1, self.depth + 1)
            self.r.makeChildren()
            self.l.makeChildren()

nodes = set()
the_tree = tree(0, 0)

count = 0
for nod in nodes:
    if nod.isValid():
        count += 1
    else:
        pass

print(count)
'''
# above was bad, I just thought to do this more dynamically

# Another day, I realized that the top traversal can tell us about the bottom

# Top is binary tree of depth 20, we will end up at one of 21 points

bucket = {}

class tree:
    def __init__(self, depth, position):
        self.depth = depth
        self.position = position
        if depth < 20:
            self.lt = tree(self.depth + 1, self.position - 1)
            self.rt = tree(self.depth + 1, self.position + 1)
        elif depth == 20:
            if self.position in bucket:
                bucket[int(self.position)] += 1
            elif self.position not in bucket:
                bucket[int(self.position)] = 1
            else:
                print("Uh Oh")
        else:
            print("Uh Oh")

root = tree(0, 0)
del(tree)
print(bucket)

# Each time it gets to the halfway point, it has the same number of ways to get home

sum = 0
for key in bucket:
    sum += bucket[key] ** 2

print(sum)

