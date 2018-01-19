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
	bfs(start) {
		let q = [];

		for (let v of this.vertexes) {
			v.color = 'white';
			v.parent = null;
		}

		start.color = 'gray';
		q.push(start);

		while(q.length > 0) {
			let peekVertex = q[0];

			// console.log(peekVertex.value);

			for (let e of peekVertex.edges) {
				let v = e.destination;

				if (v.color === 'white') {
					v.color = 'gray';
					v.parent = peekVertex;
					q.push(v);
				}
			}

			q.shift();
			peekVertex.color = 'black';
		}
	}

	/**
	 * Find a vertex by its value
	 * 
	 * Return null if the vertex isn't found
	 */
	findVertex(value) {
		let q = [];

		for (let v of this.vertexes) {
			v.color = 'white';
			v.parent = null;
		}

		let start = this.vertexes[0];

		if (start.value === value) return start;
		start.color = 'gray';
		q.push(start);

		while (q.length > 0) {
			let peekVertex = q[0];

			for (let e of peekVertex.edges) {
				let v = e.destination;

				if (v.value === value) return v;

				if (v.color === 'white') {
					v.color = 'gray';
					v.parent = peekVertex;
					q.push(v);
				}
			}

			q.shift();
			peekVertex.color = 'black';
		}

		return null;
	}

	/**
	 * Print out the route from the start vert back along the parent
	 * pointers (set in the previous BFS)
	 */
	route(start) {
		let nodes = [];
		let node = start;

		while (node.parent) {
			// console.log(node.value);
			nodes.push(node.value)
			node = node.parent;
		}

		// console.log(node.value);
		nodes.push(node.value);

		const finalStr = nodes.join(' -> ')
		console.log(finalStr);
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

// graph.bfs(graph.vertexes[0]);
// console.log(graph.findVertex('HostJ'));
// graph.route(graph.vertexes[0]);

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

// // Route from one host to another

graph.bfs(hostBVert);
graph.route(hostAVert);
