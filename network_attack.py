""" Solution for http://www.checkio.org/mission/network-attack/ in Python 2.7 """

maxint = 9223372036854775807

class Node():
    def __init__(self, id, security_level):
        self.id = id
        self.security_level = security_level
        self.next_nodes = []
        self.processed = False
        self.cracked = (security_level == 0)
        self.cracked_time = 0
        
def build_nodes(matrix, node_count):
    result = []
    for i in range(node_count):
        result.append(Node(i, matrix[i][i]))
        
    for i in range(node_count):
        next_nodes = []
        for j in range(node_count):
            if i != j and matrix[i][j]:
                next_nodes.append(result[j])
        result[i].next_nodes = next_nodes
        
    return result

def get_node_to_process(nodes):
    result = None
    duration = maxint
    for node in nodes:
        if not node.processed and node.cracked and node.cracked_time < duration:
            result = node
            duration = node.cracked_time
    return result
    
def process_node(start_node):
    for node in start_node.next_nodes:
        if not node.processed:
            cracked_time = start_node.cracked_time + node.security_level
            if not node.cracked:
                node.cracked = True
                node.cracked_time = cracked_time
            else:
                node.cracked_time = min(node.cracked_time, cracked_time)
    start_node.processed = True
                
def latest_node(nodes):
    result = None
    duration = 0
    for node in nodes:
        if node.cracked_time > duration:
            result = node
            duration = node.cracked_time
    return result
    
def capture(matrix):
    node_count = len(matrix)

    if node_count == 0:
        return 0
        
    nodes = build_nodes(matrix, node_count)
    
    to_process = get_node_to_process(nodes)

    while to_process:
        process_node(to_process)
        to_process = get_node_to_process(nodes)
        
    return latest_node(nodes).cracked_time