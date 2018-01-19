const colors = {
  reset:      (string='') => `\x1b[0m${string}`
}

Object.assign(colors, {
  bright:     (string='') => `\x1b[1m${string}${colors.reset()}`,
  dim:        (string='') => `\x1b[2m${string}${colors.reset()}`,
  underscore: (string='') => `\x1b[4m${string}${colors.reset()}`,
  blink:      (string='') => `\x1b[5m${string}${colors.reset()}`,
  reverse:    (string='') => `\x1b[7m${string}${colors.reset()}`,
  hidden:     (string='') => `\x1b[8m${string}${colors.reset()}`,

  black:      (string='') => `\x1b[30m${string}${colors.reset()}`,
  red:        (string='') => `\x1b[31m${string}${colors.reset()}`,
  green:      (string='') => `\x1b[32m${string}${colors.reset()}`,
  yellow:     (string='') => `\x1b[33m${string}${colors.reset()}`,
  blue:       (string='') => `\x1b[34m${string}${colors.reset()}`,
  magenta:    (string='') => `\x1b[35m${string}${colors.reset()}`,
  cyan:       (string='') => `\x1b[36m${string}${colors.reset()}`,
  white:      (string='') => `\x1b[37m${string}${colors.reset()}`,

  bgBlack:    (string='') => `\x1b[40m${string}${colors.reset()}`,
  bgRed:      (string='') => `\x1b[41m${string}${colors.reset()}`,
  bgGreen:    (string='') => `\x1b[42m${string}${colors.reset()}`,
  bgYellow:   (string='') => `\x1b[43m${string}${colors.reset()}`,
  bgBlue:     (string='') => `\x1b[44m${string}${colors.reset()}`,
  bgMagenta:  (string='') => `\x1b[45m${string}${colors.reset()}`,
  bgCyan:     (string='') => `\x1b[46m${string}${colors.reset()}`,
  bgWhite:    (string='') => `\x1b[47m${string}${colors.reset()}`
});

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
	}
}

/**
 * Graph class
 */
class Graph {
	constructor() {
		this.vertexes = [];
	}

	/**
	 * Breadth-First search from a starting vertex
	 */
	bfs(start, cb) {
    if (!(start instanceof Vertex))
      return [];

    const nodes = [];
    const queue = [ start ];

    const white = '#FFFFFF'
    const black = '#000000';
    const grey = '#777777';

    for (let v of this.vertexes) {
      v._color = white;
      v._parent = null;
    }

    start._color = grey;

    do {

      const node = queue.shift();
      if (!(node instanceof Vertex) || node._color === black)
        continue;
      node._color = black;
      nodes.push(node);
      queue.push(...node.edges.map((edge) => {
        const dest = edge.destination;
        if (dest._color !== black)
          dest._color = grey;
        else
          return;
        dest._parent = node;
        return dest;
      }));

      if (typeof cb === 'function')
        if (cb(node) === false)
          break;

    } while (queue.length > 0);

    return nodes;
	}

	/**
	 * Find a vertex by its value
	 *
	 * Return null if the vertex isn't found
	 */
	findVertex(value) {
		for (let node of this.vertexes)
      if (node.value === value)
        return node;
    return null;
	}

	/**
	 * Print out the route from the start vert back along the parent
	 * pointers (set in the previous BFS)
	 */
	route(start) {

		let node = start;

    if (!(node instanceof Vertex))
      node = this.findVertex(node);
    if (node === null)
      return null;

    const getColor = () => {

      const colorArray = [
        colors.red,
        colors.green,
        colors.yellow,
        colors.blue,
        colors.magenta,
        colors.cyan
      ];

      let counter = 0;

      return (string) => {
        const color = colorArray[counter];
        if (++counter >= colorArray.length)
          counter = 0;
        return color(string);
      };

    };

    let route = '';
    const color = getColor();

    while (node instanceof Vertex) {
      route = `${route}${color(node.value)}`;
      node = node._parent;
      if (node instanceof Vertex)
        route = `${route} -> `;
    }

    return route;
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

if (args.length !== 2) {
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

// Route from one host to another

graph.bfs(hostBVert);
console.log(graph.route(hostAVert));
