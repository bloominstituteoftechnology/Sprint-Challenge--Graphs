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
      if(vertex.value === value) {
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
    // !!! IMPLEMENT ME
    
    const queue = [];
    for (let vert of this.vertexes) {
      vert.color = 'white';
    }
    start.color = "gray";

    queue.push(start);
    
    start.visited = true;
    while(queue.length > 0) {
      const vertex = queue[0];
      for(let edge of vertex.edges) {
        if(edge.destination.color === 'white') {
          queue.push(edge.destination);
          edge.destination.color = 'gray'
          edge.destination.parent = vertex;
          edge.destination.visited = true;

        }
      }
      queue.shift();
      vertex.color = 'black';
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
    // !!! IMPLEMENT ME
    //console.log(" This is the result object: ",start.value);
    let valu = start;
    let cancat = "";
    while(valu.parent) {
      cancat += `${valu.value} --> `;
      valu = valu.parent;
    }
     cancat += valu.value;
     console.log(cancat);
     return cancat;
  }

  /**
   * Show the route from a starting vert to an ending vert.
   */
  route(start, end) {
    // Do BFS and build parent pointer tree
    this.bfs(end);
    // console.log(" Start node at route: ",start);
    // const groups  = [];
    // this.vertexes.forEach(vert => {
    //   // vert.color = "white";
    //   vert.parent = null;
    //   let vertex = this.findVertex(vert.value);
    //   if(end.value === vertex.value) {
    //     if(!vert.found) {
    //       groups.push(this.bfs(vert));
    //     }
    //   }
    // })
    // this.vertexes.forEach(vert => {
    //   vert.found = false;
    // })

    // Show the route from the start
    this,this.outputRoute(start);
    // for(let i of groups) {
    //   //console.log("connected groups ", i.value);
    //     for(let j in i) {
    //       //console.log("any connected groups ", i[j]);
    //       //console.log(i[j].value);
    //       if(i[j].value === start.value) {
    //         //console.log(i[j]);
    //         this.outputRoute(i[j]);
    //     }   
    //   }
    // }
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
