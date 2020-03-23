# https://graphviz.readthedocs.io/en/stable/manual.html
from graphviz import Graph, Digraph


class Node:
    def __init__(self, sum=0, move=[4, 5, 6], endpoint=21, parentEdgeValue=None, id="0"):
        self.id = id
        self.sum = sum
        self.childs = []
        self.parentEdgeValue = parentEdgeValue
        for index, value in enumerate(move):
            if sum + value <= endpoint:
                self.childs.append(
                    Node(sum+value, move, endpoint, value, id+str(index)))

    def returnChildEdgeValue(self, which):
        return self.childs[which].parentEdgeValue

    def showTree(self):
        # G = Digraph('G', filename='process.gv', engine='sfdp')
        G = Digraph('G', filename='tree', format='png')
        G.node(self.id, str(self.sum))
        self.showBranch(G)

        G.render()

    def showBranch(self, G):
        for item in self.childs:
            G.node(item.id, str(item.sum))
            G.edge(self.id, item.id, label="test", color="red")
            item.showBranch(G)


root = Node()
root.showTree()
