/**
 * Edge
 */
export class Edge {
  constructor(destination, weight = 1) {
    this.destination = destination;
    this.weight = weight;
  }
}

/**
 * Vertex
 */
export class Vertex {
  constructor(value = 'vertex', color = 'white', pos = { x: -1, y: -1 }) {
    this.value = value;
    this.edges = [];
    this.color = color;
    this.pos = pos;
  }
}

/**
 * Graph
 */
export class Graph {
  constructor() {
    this.vertexes = [];
  }

  /**
   * Create a random graph
   */
  randomize(width, height, pxBox, probability = 0.6) {
    // Helper function to set up two-way edges
    function connectVerts(v0, v1) {
      v0.edges.push(new Edge(v1));
      v1.edges.push(new Edge(v0));
    }

    let count = 0;

    // Build a grid of verts
    let grid = [];
    for (let y = 0; y < height; y++) {
      let row = [];
      for (let x = 0; x < width; x++) {
        let v = new Vertex();
        //v.value = 'v' + x + ',' + y;
        v.value = 'v' + count++;
        row.push(v);
      }
      grid.push(row);
    }

    // Go through the grid randomly hooking up edges
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        // Connect down
        if (y < height - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y + 1][x]);
          }
        }

        // Connect right
        if (x < width - 1) {
          if (Math.random() < probability) {
            connectVerts(grid[y][x], grid[y][x + 1]);
          }
        }
      }
    }

    // Last pass, set the x and y coordinates for drawing
    const boxBuffer = 0.8;
    const boxInner = pxBox * boxBuffer;
    const boxInnerOffset = (pxBox - boxInner) / 2;

    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        grid[y][x].pos = {
          'x': (x * pxBox + boxInnerOffset + Math.random() * boxInner) | 0,
          'y': (y * pxBox + boxInnerOffset + Math.random() * boxInner) | 0
        };
      }
    }

    // Finally, add everything in our grid to the vertexes in this Graph
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        this.vertexes.push(grid[y][x]);
      }
    }
  }

  /**
   * Dump graph data to the console
   */
  dump() {
    let s;

    for (let v of this.vertexes) {
      if (v.pos) {
        s = v.value + ' (' + v.pos.x + ',' + v.pos.y + '):';
      } else {
        s = v.value + ':';
      }

      for (let e of v.edges) {
        s += ` ${e.destination.value}`;
      }
      console.log(s);
    }
  }

  /**
   * Depth-first Search
   */
  dfs(start) {
    const component = new Set();
    const stack = [];

    stack.push(start);
    //start.color = "gray";

    while (stack.length > 0) {
      const u = stack.pop();
      if (u.color === 'white') {
        u.color = 'gray';

        for (let e of u.edges) {
          stack.push(e.destination);
        }
      }

      // stack.pop(); // de-stack
      u.color = 'black';

      component.add(u);
    }

    return component;

    ///////////////////////////////
    // !!! IMPLEMENT ME     white = not-visited , gray = inspected , black = visited
    // const component = new Set(); // set new array 
    // const queue = []; //// the queue 

    // start.color = 'gray'; // coloring the first vertex to be inspected by bfs() for their edges 
    // queue.push(start); // we start by  pushing  the first vertex to the queue to be inspected for children  

    // while (queue.length > 0) { /// we loop queue since the queue is not empty 
    //   const node = queue[0]; /// we take the first element in the queue to be inspected  (node), FIFO

    //   for (let edge of node.edges) { //since a vertex is an object we check the edges array for edges one by one 
    //     const vertex = edge.destination;//  we access to the vertex edge = {destination:Vertex} 1edge=1destination 
    //     if (vertex.color === 'white') { /// if the color is white means not inspected 
    //       vertex.color = 'gray'; // we visited it , so  we color it to grey 
    //       queue.push(vertex); // we push it to queue to follow the gray mother already 
    //     }
    //   }

    //   queue.shift(); // we dequeue one by one 
    //   node.color = 'black'; // we color every node in the queue to black 
    //   component.add(node); /// we add every mother (vertex)and children  (edges) to one array 
    // }

    // return component


  }

  /**
   * Get the connected components
   */
  getConnectedComponents() {
    const componentsList = [];

    for (let v of this.vertexes) {
      if (v.color === 'white') {
        const component = this.dfs(v);
        componentsList.push(component);
      }
    }

    return componentsList;
  }
}
