"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        max_value = self.head.value
        current = self.head
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value


class Queue():
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, value):
        self.queue.add_to_tail(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.remove_from_head()
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = DoublyLinkedList()

    def push(self, value):
        self.stack.add_to_tail(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.remove_from_tail()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('that vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add starting_vertex
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create set for visiting verticies
        visited_vertices = set()
        # while plan_to_visit is not empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if it has not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark as visited, (add to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neghbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        # """
        # Print each vertex in depth-first order
        # beginning from starting_vertex.
        # """
        # create a plan_to_visit stack and add starting_vertex
        # print('DFT')
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create set for visiting verticies
        visited_vertices = set()
        # while plan_to_visit is not empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex on the stack
            current_vertex = plan_to_visit.pop()
            # if it has not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark as visited, (add to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neghbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)
