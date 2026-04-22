class Node:  # define Node class for AND-OR graph representation

    def __init__(self, name, node_type):  # constructor to initialize node

        self.name = name  # store node name (e.g., Income Check, Approve)

        self.type = node_type  # store node type (AND or OR)

        self.children = []  # initialize list to store child nodes

        self.cost = 0  # initialize cost of node

        self.heuristic = 0  # initialize heuristic value of node

    def add_child(self, node):  # method to add a child node

        self.children.append(node)  # append given node to children list