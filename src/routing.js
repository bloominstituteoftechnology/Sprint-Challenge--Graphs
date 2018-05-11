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
  constructor(value = "vertex") {
    this.value = value;
    this.edges = [];
    this.flag = false;
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

  findVertex(value) {
    for (let vert of this.vertexes) {
      if (vert.value == value) {
        return vert;
      }
    }
    return null;
  }

  bfs(start) {
    let queue = [start];

    start.flag = true;

    
    while (queue.length > 0) {
      const q0 = queue[0];
      
      for (let edge of q0.edges) {
        if (edge.destination.flag === false) {
        queue.push(edge.destination);
        edge.destination.flag = true;
        edge.destination.parent = q0;
        }
      }
      queue.shift();
    }
  }

  outputRoute(start) {
    let currentVertex = start;
    let route = "";
    while(currentVertex != null) {
      route += currentVertex.value;
      if(currentVertex.parent != null) route += " --> ";
      currentVertex = currentVertex.parent;
    }
    console.log(route);
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
  console.error("usage: routing hostA hostB");
  process.exit(1);
}

// Build the entire Internet
// (it's only a model)
const graph = new Graph();
const vertA = new Vertex("HostA");
const vertB = new Vertex("HostB");
const vertC = new Vertex("HostC");
const vertD = new Vertex("HostD");
const vertE = new Vertex("HostE");
const vertF = new Vertex("HostF");
const vertG = new Vertex("HostG");
const vertH = new Vertex("HostH");

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
  console.error("routing: could not find host: " + args[0]);
  process.exit(2);
}

const hostBVert = graph.findVertex(args[1]);

if (hostBVert === null) {
  console.error("routing: could not find host: " + args[1]);
  process.exit(2);
}

// Show the route from one host to another

graph.route(hostAVert, hostBVert);