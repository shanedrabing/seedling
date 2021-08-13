__author__ = "Shane Drabing"
__license__ = "MIT"
__email__ = "shane.drabing@gmail.com"


# IMPORTS


import statistics


# ENUMS


class Sym:
    HORZ = "─"
    VERT = "│"
    RGHT = "╭"
    LEFT = "╰"
    LTEE = "┐"
    BTEE = "┤"
    RTEE = "┘"


# CLASSES


class Node:
    counter = 0

    def __init__(self, key, tip=False):
        self.key = str(key)
        self.tip = tip
        self.left = None
        self.right = None

    def __str__(self):
        return self.key

    __repr__ = __str__

    def __lt__(self, other):
        return (
            (self.num_children(), self.key) <
            (other.num_children(), other.key)
        )

    def __iter__(self):
        if self.tip:
            yield self
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right

    def num_children(self):
        return (
            1 +
            (self.left.num_children() if self.left else 0) +
            (self.right.num_children() if self.right else 0)
        )

    def add_child(self, other):
        if self is other:
            return

        if self.left is None:
            self.left = other
        elif self.right is None:
            self.right = other
        else:
            raise ValueError("too many kids")

    def connect(self, other, name=None):
        if name is None:
            parent = Node(Node.counter)
        else:
            parent = Node(name)
        Node.counter += 1
        n1, n2 = sorted((self, other))
        parent.add_child(n1)
        parent.add_child(n2)
        return parent

    def pretty(self, direct=Sym.HORZ, depth=0, connect=set()):
        forks = ("", Sym.RTEE, Sym.LTEE, Sym.BTEE)

        has_left = isinstance(self.left, Node)
        has_right = isinstance(self.right, Node)
        end = forks[(2 * has_left) + has_right]
        meat = f" {self.key} {end}".rstrip()

        newdepth = depth + len(meat)
        newconnect = connect | {newdepth}

        padding = "".join(
            Sym.VERT if i in connect else " "
            for i in range(depth)
        )

        string = str()

        if has_right:
            mod = {depth} if (direct == Sym.RGHT) else set()
            string += self.right.pretty(Sym.RGHT, newdepth, newconnect - mod)

        string += padding + direct
        if not end:
            string += Sym.HORZ
        string += meat + "\n"

        if has_left:
            mod = {depth} if (direct == Sym.LEFT) else set()
            string += self.left.pretty(Sym.LEFT, newdepth, newconnect - mod)

        if depth == 0:
            lst = string.split("\n")
            pad = max(map(lambda x: x.find(Sym.HORZ), lst))
            for i, x in enumerate(lst):
                if Sym.HORZ in x and x.find(Sym.HORZ):
                    yay = pad - x.find(Sym.HORZ)
                    lst[i] = x.replace(Sym.HORZ, Sym.HORZ * yay)
            return "\n".join(lst)

        return string


# FUNCTIONS


def node_distance(n1, n2, dist):
    return statistics.mean(
        dist[(v1.key, v2.key)]
        for v1, v2 in itertools.product(n1, n2)
    )


def next_connection(nodes, dist):
    d, n1, n2 = max((
        (node_distance(*pair, dist), *pair)
        for pair in itertools.combinations(nodes, 2)
    ), key=lambda x: x[0])

    nodes.remove(n1)
    nodes.remove(n2)

    parent = n1.connect(n2, "%.0f" % (d * 100))
    nodes.append(parent)


# SCRIPT


if __name__ == "__main__":
    import csv
    import itertools
    import sys

    if len(sys.argv) != 3:
        sys.exit(1)

    # read pairwise distance calculations
    keys = set()
    dist = dict()
    with open(sys.argv[1], encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for *k, v in reader:
            k = tuple(k)
            v = eval(v)
            keys |= set(k)
            dist[k] = v
            dist[k[::-1]] = v

    # list of Nodes
    nodes = [Node(k, tip=True) for k in keys]

    # combine Nodes until one remains
    while len(nodes) > 1:
        next_connection(nodes, dist)

    # the last node is our root
    root = next(iter(nodes))
    print(root.pretty(), file=open(sys.argv[2], "w", encoding="utf-8"))
