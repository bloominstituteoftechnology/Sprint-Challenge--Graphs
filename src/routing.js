class Edge {
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

class Vertex {
  constructor(value = "vertex") {
    this.value = value;
    this.edges = [];
  }
}

class Graph {
  constructor() {
    this.vertexes = [];
  }
  // finds if a vertex exists and returns the value, else returns null
  findVertex(value) {
    let found = this.vertexes.find(val => { 
      return val.value === value; // returns value that matches query value
    });
    if (!found) {
      found = null; // if not found, assigns from undefined to null
    }
    return found; // return result
  }
  // bfs implementation
  bfs(start) {
    const queue = []; // initialize the queue array
    for (let v of this.vertexes) { // iterate over each vertex in graph
      v.color = 'white'; // assigns color to white to indicate it has not been visited
      v.parent = null; // initializes parent key on object
    }
    start.color = 'gray'; // assigns active vertex to be gray per pseudocode instruction...could be omitted 
    queue.push(start); // pushes start value into the queue to begin operation
    while (queue.length > 0) { // checks if queue is empty and loops otherwise
      const currentVert = queue[0]; // assigns current as index zero following FIFO
      for (let edge of currentVert.edges) { // iterates over edges of vertex
        let next = edge.destination // assigns next to be the destination of the vertex
        if (next.color === 'white') { // checks if vertex has been visited
          next.color = 'gray'; // change to working color if so
          next.parent = currentVert; // assigns parent key of next as the current vertex
          queue.push(next); // pushes the next vertex to the queue
        }
      }
      currentVert.color = 'black'; // sets visited color to black
      queue.shift(); // shifts current off of the queue
    }
  }
  // outputs results to console
  outputRoute(start) {
    let route = []; // initialize an array to hold the route
    while (start) { // runs while additional backwards travel path exists
      route = [...route].concat(start.value); // assigns route to old route plus new vertex moving backwards
      start = start.parent; // reassigns start, will be checked in next potential loop cycle
    }
    const finalOutput = route.join(' --> '); // join array with arrow as specified in pseudocode
    console.log(finalOutput); // console log the output
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
