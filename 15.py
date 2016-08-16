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
