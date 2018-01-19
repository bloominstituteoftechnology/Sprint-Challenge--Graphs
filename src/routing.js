const Queue = require('./queue.js');
const ansiregex = require('./ansi-regex.js');
const colors = {
    Reset       : "\x1b[0m",
    Bright      : "\x1b[1m",
    Dim         : "\x1b[2m",
    Underscore  : "\x1b[4m",
    Blink       : "\x1b[5m",
    Reverse     : "\x1b[7m",
    Hidden      : "\x1b[8m",
    
    FgBlack     : "\x1b[30m",
    FgRed       : "\x1b[31m",
    FgGreen     : "\x1b[32m",
    FgYellow    : "\x1b[33m",
    FgBlue      : "\x1b[34m",
    FgMagenta   : "\x1b[35m",
    FgCyan      : "\x1b[36m",
    FgWhite     : "\x1b[37m",
    
    BgBlack     : "\x1b[40m",
    BgRed       : "\x1b[41m",
    BgGreen     : "\x1b[42m",
    BgYellow    : "\x1b[43m",
    BgBlue      : "\x1b[44m",
    BgMagenta   : "\x1b[45m",
    BgCyan      : "\x1b[46m",
    BgWhite     : "\x1b[47m"
};

const cI = [
    colors.FgCyan,
    colors.FgMagenta,
    colors.FgYellow,
    colors.FgRed,
    colors.FgGreen,
    colors.FgWhite,
    colors.FgCyan,
    colors.FgMagenta,
    colors.FgYellow,
    colors.FgRed,
    colors.FgGreen,
    colors.FgWhite
]

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
	bfs(start, colors = {white: '#ffffff', gray: '#efefef', black: '#3f3f3c'}) {
	    // !!! IMPLEMENT ME
	 	const queue = new Queue();
	 	const visited = [];
	
		for (let v in this.vertexes) {
	 		// if (!this.vertexes[v].color) this.vertexes[v].color = 'colors.white';
	 		this.vertexes[v].color = 'colors.white';
	    }
	
		start.color = colors.gray;
	 	start.parent = null;
	    queue.enqueue(start);
        visited.push(start);
	
	    while (!queue.isEmpty()) {
	        let u = queue.next();  // Peek at head of queue, but do not dequeue!
		    for (let v in u.edges) {
		        if (u.edges[v].destination.color !== colors.black) {
					u.edges[v].color = colors.gray;
					u.edges[v].destination.parent = u;
					u.edges[v].destination.theme = 3;
	
					queue.enqueue(u.edges[v].destination);
					visited.push(u.edges[v].destination);
	            }
	        }
			queue.dequeue();
	 		u.color = colors.black;
		}

		return visited;
	}

	/**
	 * Find a vertex by its value
	 * 
	 * Return null if the vertex isn't found
	 */
	findVertex(value) {
		for (let vert in this.vertexes) {
		    if (this.vertexes[vert].value === value) return this.vertexes[vert];
		}
		return null;
	}

	/**
	 * Print out the route from the start vert back along the parent
	 * pointers (set in the previous BFS)
	 */
	route(start) {
	    
	    let path = "";
		let parent = start;
		let cnt = 0;
		while (parent !== null) {
		    path += (path === "") ? `${cI[cnt]}${parent.value}` : ` --> ${cI[cnt]}${parent.value}`;
		    parent = parent.parent;
		    cnt++;
		}

        path = `${colors.BgBlack}  ` + path + '  ';
		
		let formatFlag = false;
		
		//const strLen = path.replace(ansiregex(), ' ').split('').reduce((reduced, char) => {
		//    console.log(char)
		//    if (formatFlag && char === 'm') {
		//        formatFlag = false;
		//        return reduced;
		//    } else if (!formatFlag && char === '\\') {
		//       formatFlag = true;
		//        return reduced;
		//   } else if (char === '$') {
		//        return reduced;
		//    } else {
		//        return reduced + 1;
		//    }
        //   //formatFlag = (formatFlag && char === 'm') ? formatFlag = false : formatFlag;
		//}, 0);

        const strLen = path.replace(ansiregex(), ' ').length;

        console.log(colors.BgBlack + colors.FgWhite + '░' + '░'.repeat(strLen - 5) + '░' + colors.Reset);
		console.log(colors.BgBlack + colors.FgWhite + '░' + path + colors.FgWhite + '░' + colors.Reset);
		console.log(colors.BgBlack + colors.FgWhite + '░' + '░'.repeat(strLen - 5) + '░' + colors.Reset);
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

// Route from one host to another

graph.bfs(hostBVert);
graph.route(hostAVert);
