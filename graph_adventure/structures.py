class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)

    def dequeue(self):
        if self.storage.head is None:
            return None
        else:
            old_head = self.storage.head.value
            self.storage.remove_head()
            return old_head

    def len(self):
        head = self.storage.head
        if head is None:
            return 0
        elif head.get_next() is None:
            return 1
        else:
            count = 1
            while head.get_next() is not None:
                count += 1
                head = head.get_next()
            return count


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_index = Node(value)
        if self.tail is not None:
            self.tail.set_next(new_index)
        else:
            self.head = new_index
        self.tail = new_index

    def remove_head(self):
        # self.head = None
        if self.head is not None:
            new = self.head.next_node
            val = self.head.get_value()
            del self.head
            self.head = new
            if self.head is None:
                del self.tail
                self.tail = None
            return val

    def contains(self, value):
        current = self.head
        while 1:
            if current is None:
                return False
            elif current.value == value:
                return True
            else:
                current = current.next_node

    def get_max(self):
        if self.head is None:
            return None
        max_val = self.head.get_value()
        current = self.head
        while current is not None:
            if current.get_value() > max_val:
                max_val = current.get_value()
            current = current.get_next()
        return max_val

    
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        if v is not None:
            self.vertices[v] = set()
        else:
            return "Error: Vertex can not be none"

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2:
            self.vertices[vertex1].add(vertex2)

    def bft(self, starting_point):
        q = Queue()
        visited = []
        q.enqueue(starting_point)
        while q.len() is not 0:
            n = q.dequeue()
            if n not in visited:
                visited.append(n)
                for i in self.vertices[f"{n}"]:
                    q.enqueue(f"{i}")
        return visited

    def dft(self, starting_point, next_set=[], visited=[]):
        if starting_point not in visited:
            visited.append(starting_point)
            for child in self.vertices[f"{starting_point}"]:
                if child not in visited:
                    self.dft(child, visited)
        return visited[1::] if visited[1:] else "No children"

    def dfts(self, starting_point):
        visited = []
        stack = []
        stack.append(starting_point)
        while len(stack) > 0:
            visited.append(stack.pop(0))
            for node in self.vertices[f"{visited[len(visited)-1]}"]:
                if node not in visited:
                    stack.append(node)
        return visited

    def bfs(self, starting_point, value):
        a = self.bft(starting_point)
        if str(value) in a:
            return True
        return False

    def dfs(self, starting_point, value):
        a = self.dfts(starting_point)
        if str(value) in a:
            return True
        return False