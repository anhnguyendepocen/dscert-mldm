import sys

# a class representing a node label
# using paired kmers
#
# slots:
#   _first: the first kmer in pair
#   _second: the second kmer in pair
class PairedKmers:
    # initialize from string with format
    # <first>|<second>
    def __init__(self, string):
        self._first, self._second = string.split("|")

    # return string representation of label with format
    # <first>|<second>
    def __repr__(self):
        return self._first + "|" + self._second

    # return the first kmer in pair
    def first(self):
        return self._first

    # return the second kmer in pair
    def second(self):
        return self._second

# a class to represent nodes in a DeBruijn graph
#
# slots:
#   _label: the paired k-1 mer label
#   _targets: list of target nodes for outgoing edges
class Node:
    # intialize node with label and empty targets list
    def __init__(self, label):
        self._label = label
        self._targets = []

    # get a string representation of node in format
    # <label> -> <comma_separated_list_of_target_labels>
    def __repr__(self):
        target_labels = [target.label_string() for target in self._targets]
        targets_string = ",".join(target_labels)
        return self.label_string() + " -> " + targets_string

    # return the node label
    def label(self):
        return self._label

    # return node label as string
    def label_string(self):
        return self.label().__repr__()

class DoubleList:
    def __init__(self, node, prev_item=None, next_item=None):
        self._node = node
        self._prev_item = prev_item
        self._next_item = next_item

class Path:
    def __init__(self, k, d):
        self._k = k
        self._d = d
        self._head = None
        self._tail = None

    @staticmethod
    def _string_helper(kmers):
        out = ""
        for kmer in kmers:
            if len(out) == 0:
                out = kmer
            else:
                out += kmer[-1]
        return out

    def get_string(self):
        prefix_string = self._string_helper([node.label().first() for node in self.nodes()])
        suffix_string = self._string_helper([node.label().second() for node in self.nodes()])

        n = len(prefix_string)
        prefix_overlap = prefix_string[self._k + self._d:]
        suffix_overlap = suffix_string[:n - self._k - self._d]

        if prefix_overlap != suffix_overlap:
            return None
        else:
            return prefix_string + suffix_string[-(self._k + self._d):]

    def is_empty(self):
        return self._head is None and self._tail is None

    def append(self, node):
        item = DoubleList(node)
        if self.is_empty():
            self._head = self._tail = item
        else:
            tail_item = self._tail
            tail_item._next_item = item
            item._prev_item = tail_item
            self._tail = item

    def nodes(self):
        current = self._head
        while current is not None:
            yield current._node
            current = current._next_item

    def __repr__(self):
        node_labels = [node._label for node in self.nodes()]
        return " -> ".join([label.__repr__() for label in node_labels])

def build_pairedend_path(edges, k, d):
    path = Path(k, d)
    for edge in edges:
        source_label, target_label = [PairedLabel(s.strip()) for s in edge.split("->")]
        if path.is_empty():
            source = Node(source_label)
            path.append(source)
        target = Node(target_label)
        path.append(target)

    return path

def readdat(filename):
    with open(filename, 'r') as f:
        k, d = [int(s) for s in f.readline().strip().split()]
        edges = []
        for line in f:
            edges.append(line.strip())
        return edges, k, d

def main(filename):
    edges, k, d = readdat(filename)
    path = build_pairedend_path(edges, k, d)
    string = path.get_string()
    print string

# this is here so this plays nicely with ipython %loadpy magic
if __name__ == '__main__' and 'get_ipython' not in dir():
    filename = sys.argv[1]
    main(filename)
