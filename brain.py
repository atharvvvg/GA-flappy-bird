import node
import connection
import random

class Brain:
    def __init__(self, inputs, clone=False):
        self.connections = []
        self.nodes = []
        self.inputs = inputs
        self.net = []
        self.layers = 2

        if not clone:
            # input nodes
            for i in range(0, self.inputs):
                self.nodes.append(node.Node(i))
                self.nodes[i].layer = 0
            # bias node
            self.nodes.append(node.Node(3))
            self.nodes[3].layer = 0
            # output node
            self.nodes.append(node.Node(4))
            self.nodes[4].layer = 1

            # Create connections
            for i in range(0, 4):
                self.connections.append(connection.Connection(self.nodes[i], self.nodes[4], random.uniform(-1, 1)))

    def connect_nodes(self):
        for node in self.nodes:
            node.connections = []
        for connection in self.connections:
            connection.from_node.connections.append(connection)

    def generate_net(self):
        self.connect_nodes()
        self.net = []
        for j in range(0, self.layers):
            for node in self.nodes:
                if node.layer == j:
                    self.net.append(node)

    def feed_forward(self, vision):
        for i in range(0, self.inputs):
            self.nodes[i].output_value = vision[i]

        self.nodes[3].output_value = 1

        for node in self.net:
            node.activate()
        
        output_value = self.nodes[4].output_value

        for node in self.nodes:
            node.input_value = 0
        
        return output_value
        
    def clone(self):
        clone=Brain(self.inputs, True)

        for n in self.nodes:
            clone.nodes.append(n.clone())

        for c in self.connections:
            clone.connections.append(c.clone(clone.getNode(c.from_node.id),clone.getNode(c.to_node.id)))

        clone.layers=self.layers
        clone.connect_nodes()
        return clone
    
    def getNode(self, id):
        for n in self.nodes:
            if n.id==id:
                return n

    def mutate(self):
        if random.uniform(0,1)<0.8:
            for i in range(0, len(self.connections)):
                self.connections[i].mutate_weight()