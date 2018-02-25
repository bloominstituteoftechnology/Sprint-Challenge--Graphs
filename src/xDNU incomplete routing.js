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
  constructor(value = "vertex") {
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
  constructor() {
    this.stack = [];
    this.vertexes = [];
  }

  /**
   * This function looks through all the vertexes in the graph and returns the
   * first one it finds that matches the value parameter.
   *
   * Used from the main code to look up the verts passed in on the command
   * line.
   *
   */
  findVertex(value) {
    for (let v of this.vertexes) {
      if (v.value === value) {
        return v;
      }
    }
    return null;
  }

  /**
   * Breadth-First search from a starting vertex. This should log parent
   * pointers back from neighbors to their parent.
   *
   * @param {Vertex} start The starting vertex for the BFS
   */
  bfs(start) {
    if (start === undefined) {
      start = this.vertexes[0];
    } else {
      start = this.vertexes[start];
    }
    // make stack local so you don't have to type this.stack every time
    let stack = this.stack;

    // if the stack has no length, push the start to the stack - shouldn't be needed as it was pushed in find vertex
    // if (this.stack.length === 0) stack.push(start);

    // initialize a variable to the zeroth index of the stack
    let u = stack[0];

    // iterate through the edges of that variable
    u.edges.forEach(e => {
      // set vert to the destination = next node
      let vert = e.destination;

      // if that vert is white
      if (vert.color === "white") {
        // set the color to grey indication we're investigating it
        vert.color = "grey";
        // set its parent pointer
        vert.parent = u;
        // push the vert to the stack for future use
        stack.push(vert);
      }
    });

    // we're done investigating this vert so make it black
    u.color = "black";
    // remove it from the stack
    stack.shift();
  }

  /**
   * Print out the route from the start vert back along the parent
   * pointers (which should have been set in the previous BFS)
   *
   * @param {Vertex} start The starting vertex to follow parent
   *                       pointers from
   */
  outputRoute(start) {
    // start with an empty string to track our route
    let route = "";
    // set the node to the starting vertex
    let node = start;
    // while there are still nodes (meaning while the node doesn't return null, as it will once the parent value reaches the end of the line)
    while (node) {
      // append the route with the following
      route += ` --> ${node.value}`;
      // set the node to the node's parent
      node = node.parent;
    }
    // log the route
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
