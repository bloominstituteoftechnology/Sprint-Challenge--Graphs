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
    for (let v of this.vertexes) {
      console.log(`value of v is ${v.value}`);
      console.log(`value to find is ${value}`);
      if (v.value === value) {
        return v;
      }
    }
    return null; // value could not be found
  }

  /**
   * Breadth-First search from a starting vertex. This should keep parent
   * pointers back from neighbors to their parent.
   *
   * @param {Vertex} start The starting vertex for the BFS
   */
  bfs(start) {
    const queue = [];
    for (let v of this.vertexes) {
      v.color = "white"; // mark all vertexes as unvisited
      v.parent = null; // initialize parent property
    }

    start.color = "gray"; // start is being visited
    queue.push(start);

    while (queue.length > 0) {
      let current = queue[0];

      for (let edge of current.edges) {
        let vertex = edge.destination;
        if (vertex.color === "white") {
          vertex.color = "gray";
          vertex.parent = current; // generate a parent link for edges
          queue.push(vertex); // add neighboring nodes to queue
        }
      }
      current.color = "black"; // current has been visited
      queue.shift(); // remove current;
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
    const stack = [];
    const result = [];

    let startVertex;
    for (let v of this.vertexes) {
      if (v.value == start) {
        startVertex = v;
      }
    }

    let path = "";
    stack.push(startVertex.value);

    while (stack.length > 0) {
      let current = stack[stack.length - 1];
      if (current.parent) {
        stack.push(current.parent.value);
      }
      result.unshift(stack.shift());
    }

    for (let route of result) {
      path += `${route} `;
    }
    // path = path.slice(0, path.length - 1);
    console.log(path);
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
