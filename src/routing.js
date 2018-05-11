// Search for "!!! IMPLEMENT ME" comments

/**
 * Edge class
 */
class Edge {
  constructor(destination, weight=1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex class
 */
class Vertex {
  constructor(value='vertex') {
    this.value = value;
    this.edges = [];
    this.color = 'white';
    this.parent = null;
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
    this.queue = [];
    // this.found = [];
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
    return this.vertexes.find(element => {
      if (element.value === value) {
        return element;
      } else {
        return null;
      }
    });
  }

  /**
   * Breadth-First search from a starting vertex. This should keep parent
   * pointers back from neighbors to their parent.
   *
   * @param {Vertex} start The starting vertex for the BFS
   */
  bfs(start) {
    // !!! IMPLEMENT ME

    const parentTree = [];

    let { queue } = this;
    start.color = 'gray';
    queue.push(start)
    while (queue.length > 0) {

      let u = queue[0];

      for (let v of u.edges) {
        let { destination: vert } = v;
        if (vert.color === 'white') {
          
          vert.color = 'gray';
          vert.parent = u;     // <-- Keep a parent link
          queue.push(vert);
          if (u.color === 'gray') parentTree.push(u.value); 
        }
    
      }
      queue.shift();
      u.color = 'black';
    }
    console.log({parentTree});
    return parentTree;
    // console.log({start});
    // let { found, queue } = this;
    // queue.push(start);
    // found.push(start);
    // while (queue.length > 0) {
    //   console.log('queue', queue);
    //   queue[0].edges.forEach((edge) => {
    //     if (!found.includes(edge.destination)) {
    //       found.push(edge.destination);
    //       queue.push(edge.destination);
    //       edge.destination.parent = queue[0];
    //     }
    //   });
    //   queue.shift();
    // }
    // // console.log('found', found);
    // return found;
  }

  /**
   * Print out the route from the start vert back along the parent
   * pointers (set in the previous BFS)
   *
   * @param {Vertex} start The starting vertex to follow parent
   *                       pointers from
   */
  outputRoute(start, routeArray) {
    // !!! IMPLEMENT ME
    let returnString = start.value;
    console.log(this.hostBvert.value);
    routeArray.forEach((value) => {
      if (value !== start.value) {
        returnString += ' --> ' + value;
      }
    });
    console.log(returnString);
  }

  /**
   * Show the route from a starting vert to an ending vert.
   */
  route(start, end) {
    // Do BFS and build parent pointer tree
    // this.bfs(end);

    // Show the route from the start
    this.outputRoute(start, this.bfs(end));
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
