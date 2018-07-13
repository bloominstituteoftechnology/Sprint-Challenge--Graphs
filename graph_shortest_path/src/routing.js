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
    const verts = this.vertexes;
    for (let el of verts) {
      if (el.value === value) return el;

    }
     return null;
  }

  /**
   * Breadth-First search from a starting vertex. This should keep parent
   * pointers back from neighbors to their parent.
   *
   * @param {Vertex} start The starting vertex for the BFS
   BFS(graph, startVert):
  for v of graph.vertexes:
    v.color = white
    v.parent = null   // <-- Add parent initialization

  startVert.color = gray
  queue.enqueue(startVert)

  while !queue.isEmpty():
    u = queue[0]

    for v of u.neighbors:
      if v.color == white:
        v.color = gray
        v.parent = u     // <-- Keep a parent link
        queue.enqueue(v)
    
    queue.dequeue()
    u.color = black
   
   */


  bfs(start) {
    let queue = [];
   
    const verts = this.vertexes;

    //color every verts --> white
    verts.forEach(el => {
      el.color = 'white';
      el.parent = null;
    })

    start.color = 'gray'; // make the start vert --> gray;
    queue.push(start); // push it --> queue


    while (queue.length) { // as long as length is truthy
      const u = queue.pop(); // pop out the vert

      for (let e of u.edges) { // loop over it edges 
        const v = e.destination; // grab its  destination
        if (v.color === 'white') { //  if the destination is not visited yet
          v.color = 'gray'; // make it gray
          v.parent = u; // set the destination's parent -->  vert 
          queue.push(v); // push the destination in queue 
        }
      }
      u.color = 'black' // make the vert black(visited)
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
    let print = '';
    // let currentNode = start;
    while (start.parent) {
      print += start.value + "-->";
      start = start.parent;
    }
    print += start.value;
    console.log(print);
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