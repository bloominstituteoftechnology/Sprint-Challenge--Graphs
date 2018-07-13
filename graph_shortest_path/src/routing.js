// Search for "!!! IMPLEMENT ME" comments

/* Edge class */
class Edge {
  constructor(destination, weight=1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/* Vertex class */
class Vertex {
  constructor(value='vertex', color='white') {
    this.value = value;
    this.edges = [];
    this.color = color;
    this.parent = null;
  }

  restoreDefaults() {
    this.color = "white";
    this.parent = null;
  }
}

/* Graph class */
class Graph {
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
    return this.vertexes.find(v => v.value === value) || null;
  }

  /**
   * Breadth-First search from a starting vertex. This should keep parent
   * pointers back from neighbors to their parent.
   *
   * @param {Vertex} start The starting vertex for the BFS
   */
  bfs(start) {
    this.vertexes.forEach(v => v.restoreDefaults());

    const queue = [start];
    start.color = "gray";
    
    while (queue.length) {
      const vertex = queue.shift();

      vertex.edges.forEach(e => {
        const target = e.destination;
        if (target.color === "white") {
          target.color = "gray";
          target.parent = vertex;
          queue.push(target);
        }
      });

      vertex.color = "black";
    }
  }

  /**
   * Print out the route from the start vert back along the parent
   * pointers (set in the previous BFS)
   *
   * @param {Vertex} start The starting vertex to follow parent
   *                       pointers from
   */
  outputRoute(start) {
    let vertex = start;
    let result = `\n${start.value}`;

    while (vertex.parent) {
      result += ` --> ${vertex.parent.value}`;
      vertex = vertex.parent;
    }

    console.log(result);
  }

  /* Show the route from a starting vert to an ending vert. */
  route(start, end) {
    this.bfs(end); // Do BFS and build parent pointer tree
    this.outputRoute(start); // Show the route from the start
  }
}

/* Helper function to add bidirectional edges */
function addEdge(v0, v1) {
  v0.edges.push(new Edge(v1));
  v1.edges.push(new Edge(v0));
}

/* Main */

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
