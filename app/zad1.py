# https://graphviz.readthedocs.io/en/stable/manual.html
from graphviz import Graph, Digraph


class Node:
    def __init__(self, sum=0, move=[4, 5, 6], endpoint=21, parentEdgeValue=None, id="0"):
        self.id = id
        self.sum = sum
        self.childs = []
        self.move = move
        self.result = 0
        self.endpoint = endpoint
        self.parentEdgeValue = parentEdgeValue
        for index, value in enumerate(move):
            if sum + value <= endpoint + move[len(move)-1]:
                self.childs.append(
                    Node(sum+value, move, endpoint, value, id+str(index)))

    def showTree(self):
        G = Digraph('G', filename='tree', format='png')
        G.node(self.id, "Prot\n" + str(self.sum))
        turn = "Prot"
        self.showTree_subfunc(G, turn)

        G.render()

    def showTree_subfunc(self, G, turn):
        if turn == "Prot":
            turn="Ant"
        else: 
            turn="Prot"
        for item in self.childs:
            print(item.sum, item.endpoint)
            if item.sum > item.endpoint:
                if turn=="Prot":
                    item.result = -1
                else:
                    item.result = 1
                G.node(item.id,turn +"\n"+str(item.sum)+ "\nWynik:" + str(item.result))
                G.edge(self.id, item.id, label=str(item.parentEdgeValue))
            elif item.sum == item.endpoint:
                item.result = 0
                G.node(item.id,turn +"\n"+str(item.sum)+ "\nWynik:" + str(item.result))
                G.edge(self.id, item.id, label=str(item.parentEdgeValue))
            else:
                print(item.result)
                G.node(item.id,turn +"\n"+str(item.sum))
                G.edge(self.id, item.id, label=str(item.parentEdgeValue))
                item.showTree_subfunc(G, turn)
    
    def minmax(self):
        G = Digraph('G', filename='minmax', format='png')
        G.node(self.id, "Prot\n" + str(self.sum))
        turn = "Prot"
        self.minmax_subfunc(G, turn)

        G.render()

    def minmax_subfunc(self, G, turn):
        if turn == "Prot":
            turn="Ant"
        else: 
            turn="Prot"
        for item in self.childs:
            color="black"
            if turn == "Prot" and item.parentEdgeValue == max(self.move):
                color="red"
            elif turn == "Ant" and item.parentEdgeValue == min(self.move):
                color="red"
            print(item.sum, item.endpoint)
            if item.sum > item.endpoint:
                if turn=="Prot":
                    item.result = -1
                else:
                    item.result = 1
                G.node(item.id,turn +"\n"+str(item.sum)+ "\nWynik:" + str(item.result))
                G.edge(self.id, item.id, label=str(item.parentEdgeValue), color=color)
            elif item.sum == item.endpoint:
                item.result = 0
                G.node(item.id,turn +"\n"+str(item.sum)+ "\nWynik:" + str(item.result))
                G.edge(self.id, item.id, label=str(item.parentEdgeValue), color=color)
            else:
                print(item.result)
                G.node(item.id,turn +"\n"+str(item.sum))
                G.edge(self.id, item.id, label=str(item.parentEdgeValue), color=color)
                item.minmax_subfunc(G, turn)
            
            


root = Node()
root.minmax()
