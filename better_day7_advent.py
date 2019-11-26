data = open('data_day7.txt','r').readlines()
class node_storage(object):
    def __init__(self):
        self.storage = []
    def check_for_node(self, name):
        '''
        either returns index or -1 if its not there
        pass in string of wire name
        '''
        for i, node in self.storage:
            if node.name == name:
                return i
        return -1
    #need this for having methods to store the nodes right...
class Node(object):
    """
    pass in lists of Node objects as inputs and outputs
    or pass in input as being a list with one int value.
    pass in string as name.
    gates will have integer name, their unique id
    DO NOT MAKE FIXED VALUES A NODE!!!!!!!!!!!!!!!
    WIRES WILL HAVE THEIR NAME STORED IN SELF.NAME AS STRING
    """
    unique_identifier = 0
    def __init__(self,inputs=[],outputs=[], *args):
        self.inputs_sources = inputs
        self.outputs_destinations = outputs
        self.unique_identifier = Node.unique_identifier
        Node.unique_identifier += 1
        if args:
            self.name = args
        else:
            self.name = self.unique_identifier
    def output_value(self):
        """
        this method will calll output_value method of first input source. 
        override this method for gate subclass, as they can have multiple inputs. 
        """
        if isinstance(self.inputs_sources[0], int): 
            return self.inputs_sources[0] #IF YOU STORE FIXED VALUES AS NODES THAT WILL BREAK THIS FUNCTIONALITY
        elif self.inputs_sources == []:
            raise Exception()
        else:
            return self.inputs_sources[0].output_value()
    def update_inputs(self, more_inputs):
        """
        pass in a list of node objets for the more_inputs argument. 
        """
        self.inputs_sources.extend(more_inputs)
    def update_outputs(self, more_outputs):
        """
        pass in a list of node objets for the more_inputs argument. 
        """
        self.outputs_destinations.extend(more_outputs)
class and_gate(Node):
    def output_value(self):
        if len(self.inputs_sources) != 2:
            raise Exception()
        else:
            return self.inputs_sources[0].output_value & self.inputs_sources[1].output_value
class or_gate(Node):
    def output_value(self):
        if len(self.inputs_sources) != 2:
            raise Exception()
        else:
            return self.inputs_sources[0].output_value | self.inputs_sources[1].output_value
class not_gate(Node):
    def output_value(self):
        if len(self.inputs_sources) != 1:
            raise Exception()
        else:
            return self.inputs_sources[0].output_value  ^ 65535
class lshift_gate(Node):
    def output_value(self):
        if len(self.inputs_sources) != 2:
            raise Exception()
        else:
            return self.inputs_sources[0].output_value << self.inputs_sources[1].output_value & 65535
class rshift_gate(Node):
    def output_value(self):
        if len(self.inputs_sources) != 2:
            raise Exception()
        else:
            return self.inputs_sources[0].output_value >> self.inputs_sources[1].output_value
look_up_dict = {
    'AND': and_gate,
    'OR': or_gate,
    'NOT': not_gate,
    'LSHIFT': lshift_gate,
    'RSHIFT': rshift_gate,
}
storage = node_storage()
for line in data:
    line = line.strip('\n')
    line = line.split(" ")
    right_side_item = line.pop()
    line.pop()
    left_side_items = line
    operator = 0
    operators = ['AND','OR','NOT','LSHIFT','RSHIFT']
    for item in left_side_items:
        if item in operators:
            operator = item
    if operator:
        left_side_items.remove(operator)
        new_node = look_up_dict[operator](inputs=left_side_items, outputs=[right_side_item])
        storage.storage.append(new_node)
        for item in left_side_items:
            try:
                int(item) #dont need to make fixed values a node
            except:
                if storage.check_for_node(item) == -1:
                    other_node = Node(outputs=[new_node],item) #this might not work
                    storage.storage.append(other_node)
                else:
                    storage.storage[storage.check_for_node(item)].outputs_destinations.append(new_node)
        if storage.check_for_node(right_side_item) == -1:
                    other_node = Node(inputs=[new_node],right_side_item) #this might not work
                    storage.storage.append(other_node)
                else:
                    storage.storage[storage.check_for_node(item)].inputs_sources.append(new_node)
    else:
        flag1 = 0
        try:
            int(left_side_items[0])
            flag1 = 1
        except:
            pass
        flag3 = 0
        flag4 = 0
        if flag1 == 0:
            if storage.check_for_node(left_side_items[0]) == -1:
                new_node_1 = Node(left_side_items[0])
                flag3 = 1
        if storage.check_for_node(right_side_item) == -1:
            new_node_2 = Node(right_side_item)
            flag4 = 1
        if flag3 == 1 and flag1 == 0 and flag4 == 1:
            new_node_1.outputs_destinations.append(new_node_2)
            new_node_2.inputs_sources.append(new_node_1)
            storage.storage.append(new_node_1)
            storage.storage.append(new_node_2)
        elif flag3 == 0 and flag4 == 0 and flag1 == 0:
            pass
            #WORK IN PROOGRESS
        

