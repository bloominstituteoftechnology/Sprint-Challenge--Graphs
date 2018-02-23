// Search for "!!! IMPLEMENT ME" comments
//Edge class
class Edge {
	constructor(destination, weight = 1) {
		this.destination = destination;
		this.weight = weight;
	}
}

//Vertex class
class Vertex {
	constructor(value = 'vertex') {
		this.value = value;
		this.edges = [];
	}
}

//Graph class
class Graph {
	//Constructor
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
		// pretty self explanatory - searches thru the array and matches the value.
		for (let info of this.vertexes) {
			if (info.value === value) {
				// return value if found
				return info;
			}
		}
		// if none found, return null.
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
		// standard bfs search
		const queue = [];
		for (let n of this.vertexes) {
			n.color = 'white'; // yeah I know im setting some weird state LOL I just borrowed the bfs from my graphs assignment.
			n.parent = null;
		}
		queue.push(start);

		while (queue.length) {
			//shifts vertex off queue
			let dequeue = queue.shift();
			//console.log('dequeue', dequeue);
			for (let edge of dequeue.edges) {
				//fiddles with it and makes it used
				let vertex = edge.destination;
				//console.log('vertex', vertex);
				if (vertex.color === 'white') {
					vertex.color = 'pink'; //visited
					vertex.parent = dequeue;
					queue.push(vertex);
				}
			}
			dequeue.color = 'black'; //finished with it
			console.log('vertex: ', dequeue.value, ' ', 'dq color: ', dequeue.color);
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
		// recursive function to push the route to an array and print
		let route = [start.value];
		const route_path = v => {
			if (v.parent) {
				route.push(v.parent.value);
				route_path(v.parent);
			}
		};
		route_path(start);
		console.log('path: ', route.join(' --> '));
	}

	/**
	 * Show the route from a starting vert to an ending vert.
	 */
	route(start, end) {
		// Do BFS and build parent pointer tree
		console.log('start', start, 'end', end);
		this.bfs(end);

		// Show the route from the start
		this.outputRoute(start);
	}
}

//Helper function to add bidirectional edges

function addEdge(v0, v1) {
	v0.edges.push(new Edge(v1));
	v1.edges.push(new Edge(v0));
}

//Main

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

// My output:
// C:\Users\Crites\Desktop\Lambda School Masters\Sprint-Challenge--Graphs\src>node routing.js HostE HostB
// start Vertex {
//   value: 'HostE',
//   edges:
//    [ Edge { destination: [Object], weight: 1 },
//      Edge { destination: [Object], weight: 1 } ] } end Vertex {
//   value: 'HostB',
//   edges:
//    [ Edge { destination: [Object], weight: 1 },
//      Edge { destination: [Object], weight: 1 } ] }
// vertex:  HostB   dq color:  black
// vertex:  HostA   dq color:  black
// vertex:  HostD   dq color:  black
// vertex:  HostC   dq color:  black
// vertex:  HostF   dq color:  black
// vertex:  HostG   dq color:  black
// vertex:  HostE   dq color:  black
// vertex:  HostH   dq color:  black
// path:  HostE-->HostF-->HostC-->HostA-->HostB
