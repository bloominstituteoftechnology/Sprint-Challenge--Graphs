// Search for "!!! IMPLEMENT ME" comments

/**
 * Edge class
 */
class Edge {
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex class
 */
class Vertex {
  constructor(value = 'vertex') {
    this.value = value;
    this.edges = [];
    this.parent = null;
    this.color = "white";
  }
}

/**
 * Graph class
 */
class Graph {

  /**
   * Constructor
   */
  constructor() {
    this.vertexes = [];
  }

  /**
   * This function looks through all the vertexes in the graph and returns the
   * first one it finds that matches the value parameter.
   *
   * Used from the main code to look up the verts passed in on the command
   * line.
   *
   * @param {*} value The value of the Vertex to find
   *
   * @return null if not found.
   */
  findVertex(value) {
    // !!! IMPLEMENT ME

    for (let vertex of this.vertexes) {
      if (vertex.value === value) {
        return vertex;
      }
    }
    return null;
  }

  /**
   * Breadth-First search from a starting vertex. This should keep parent
   * pointers back from neighbors to their parent.
   *
   * @param {Vertex} start The starting vertex for the BFS
   */
  bfs(start) {
    //     white = not-visited , gray = inspected , black = visited
    // const component = []; // set new array 
    const queue = []; //// the queue 

    start.color = 'gray'; // coloring the first vertex to be inspected by bfs() for their edges 
    queue.push(start); // we start by  pushing  the first vertex to the queue to be inspected for children  

    while (queue.length > 0) { /// we loop queue since the queue is not empty 
      const node = queue[0]; /// we take the first element in the queue to be inspected  (node), FIFO

      for (let edge of node.edges) { //since a vertex is an object we check the edges array for edges one by one 
        const vertex = edge.destination;//  we access to the vertex edge = {destination:Vertex} 1edge=1destination 
        if (vertex.color === 'white') { /// if the color is white means not inspected 
          vertex.color = 'gray'; // we visited it , so  we color it to grey 
          vertex.parent = node;
          queue.push(vertex); // we push it to queue to follow the gray mother already 
        }
      }

      queue.shift(); // we dequeue one by one 
      node.color = 'black'; // we color every node in the queue to black 
      //component.add(node); /// we add every mother (vertex)and children  (edges) to one array 
    }

    // return component
  }

  /**
   * Print out the route from the start vert back along the parent
   * pointers (set in the previous BFS)
   *
   * @param {Vertex} start The starting vertex to follow parent
   *                       pointers from
   */
  outputRoute(start) {
    // !!! IMPLEMENT ME
    let current = start;
    let string = ""

    while (current !== null) {
      string += current.value;
      if (current.parent !== null) {
        string += " ---->"
      }
      current = current.parent

    }
    console.log(string);
  }

  /**
   * Show the route from a starting vert to an ending vert.
   */
  route(start, end) {
    // Do BFS and build parent pointer tree
    this.bfs(end);

    // Show the route from the start
    this.outputRoute(start);
  }
}

/**
 * Helper function to add bidirectional edges
 */
function addEdge(v0, v1) {
  v0.edges.push(new Edge(v1));
  v1.edges.push(new Edge(v0));
}

/**
 * Main
 */

// Test for valid command line
const args = process.argv.slice(2);

if (args.length != 2) {
  console.error('usage: routing hostA hostB');
  process.exit(1);
}

// Build the entire Internet
// (it's only a model)
const graph = new Graph();
const vertA = new Vertex('HostA');
const vertB = new Vertex('HostB');
const vertC = new Vertex('HostC');
const vertD = new Vertex('HostD');
const vertE = new Vertex('HostE');
const vertF = new Vertex('HostF');
const vertG = new Vertex('HostG');
const vertH = new Vertex('HostH');

addEdge(vertA, vertB);
addEdge(vertB, vertD);
addEdge(vertA, vertC);
addEdge(vertC, vertD);
addEdge(vertC, vertF);
addEdge(vertG, vertF);
addEdge(vertE, vertF);
addEdge(vertH, vertF);
addEdge(vertH, vertE);

graph.vertexes.push(vertA);
graph.vertexes.push(vertB);
graph.vertexes.push(vertC);
graph.vertexes.push(vertD);
graph.vertexes.push(vertE);
graph.vertexes.push(vertF);
graph.vertexes.push(vertG);
graph.vertexes.push(vertH);

// Look up the hosts passed on the command line by name to see if we can
// find them.

const hostAVert = graph.findVertex(args[0]);

if (hostAVert === null) {
  console.error('routing: could not find host: ' + args[0]);
  process.exit(2);
}

const hostBVert = graph.findVertex(args[1]);

if (hostBVert === null) {
  console.error('routing: could not find host: ' + args[1]);
  process.exit(2);
}

// Show the route from one host to another

graph.route(hostAVert, hostBVert);
